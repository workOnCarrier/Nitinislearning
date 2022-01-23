import queue
import time

from async_concurrent.callback_scheduler import sched
from async_concurrent.yield_scheduler import scheduler


class QueueClosed(Exception):
    pass


def producer(q: queue, count: int):
    for n in range(count):
        print(f'producing {n}')
        q.put(n)
        time.sleep(1)
    print(f'Producer done')
    q.put(None)  # sentinel to mark shut down of production


def consumer(q: queue):
    while True:
        item = q.get()
        if item is None:
            break
        print(f'consuming {item}')
    print(f'Consumer done')


def callback_producer(q: queue, count: int):
    def _run(n):
        if n < count:
            print(f'producing {n}')
            q.put(n)
            sched.call_later(1, lambda: _run(n + 1))
        else:
            print('Producer done')
            q.close()

    _run(0)


def callback_consumer(id: str, q: queue):
    def _consume(result):
        try:
            item = result.result()
            print(f'consuming {id}:{item}')
            sched.call_soon(lambda: callback_consumer(id, q))
        except QueueClosed:
            print(f'Consumer done {id}')

    q.get(callback=_consume)


async def async_producer(q: queue, count: int):
    for n in range(count):
        print(f'producing {n}')
        await q.put(n)
        await scheduler.sleep(1)
    print(f'Producer done')
    q.close()
#    await q.put(None)  # sentinel to mark shut down of production


async def async_consumer(q: queue):
    try:
        while True:
            item = await q.get()
            print(f'consuming {item}')
    except QueueClosed:
        print(f'Consumer done')
