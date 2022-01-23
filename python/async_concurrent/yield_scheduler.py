from collections import deque
import time
import heapq

from async_concurrent.async_common import switch


class MyYieldScheduler:
    def __init__(self):
        self.ready = deque()  # queue for functions to execute
        self.current = None
        self.seq_no = 0
        self.sleeping = []

    async def sleep(self, delay):
        # current coroutine wants to sleep
        deadline = time.time() + delay
        self.seq_no += 1
        heapq.heappush(self.sleeping, (deadline, self.seq_no, self.current))
        self.current = None
        await switch()

    def new_task(self, gen_fun):
        self.ready.append(gen_fun)

    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                deadline, _, cor = heapq.heappop(self.sleeping)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(cor)
            self.current = self.ready.popleft()
            try:
                self.current.send(None)
                # next(self.current) -- usalbe with yield only
                if self.current:
                    self.ready.append(self.current)
            except StopIteration:
                pass


scheduler = MyYieldScheduler()
