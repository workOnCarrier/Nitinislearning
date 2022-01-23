from collections import deque

from async_concurrent.callback_scheduler import sched
from async_concurrent.producer_consumer import QueueClosed
from async_concurrent.yield_scheduler import scheduler


class Awaitable:
    def __await__(self):
        yield


def switch():
    return Awaitable()


class AsyncCallbackQueue:
    def __init__(self):
        self.items = deque()
        self.waiting = deque()
        self._closed = False

    def close(self):
        self._closed = True
        while self.waiting:
            func = self.waiting.popleft()
            sched.call_soon(func)

    def put(self, item):
        self.items.append(item)
        if self.waiting:
            func = self.waiting.popleft()
            sched.call_soon(func)

    def get(self, callback):
        # wait until an item is available and return it
        if self.items:
            callback(Result(value=self.items.popleft()))
        else:
            if self._closed:
                callback(Result(exc=QueueClosed()))
            else:
                self.waiting.append(lambda: self.get(callback))


class Result:
    def __init__(self, value=None, exc=None):
        self.value = value
        self.exc = exc

    def result(self):
        if self.exc:
            raise self.exc
        return self.value


class AsyncAwaitQueue:
    def __init__(self):
        self.items = deque()
        self.waiting = deque()
        self._closed = False

    def close(self):
        self._closed = True
        while self.waiting and not self.items:
            scheduler.ready.append(self.waiting.popleft())

    async def put(self, item):
        if self._closed:
            raise QueueClosed()
        self.items.append(item)
        if self.waiting:
            scheduler.ready.append(self.waiting.popleft())

    async def get(self):
        while not self.items:
            if self._closed:
                raise QueueClosed()
            self.waiting.append(scheduler.current)
            scheduler.current = None
            await switch()
        item = self.items.popleft()
        return item