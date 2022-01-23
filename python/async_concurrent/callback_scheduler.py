from collections import deque
import time
import heapq


class MyScheduler:
    def __init__(self):
        self.ready = deque()  # queue for functions to execute
        self.sleeping = []
        self.seq = 0

    def call_soon(self, func):
        self.ready.append(func)

    def call_later(self, delay, func):
        self.seq += 1
        deadline = time.time() + delay
        # self.sleeping.append((deadline, func))
        # self.sleeping.sort()
        heapq.heappush(self.sleeping, (deadline, self.seq, func))

    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                # deadline, func = self.sleeping.pop(0)
                deadline, _, func = heapq.heappop(self.sleeping)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.call_soon(func)
            while self.ready:
                func = self.ready.popleft()
                func()



sched = MyScheduler()
