import time

from async_concurrent.async_common import switch
from async_concurrent.yield_scheduler import scheduler


def countdown(n):
    while n > 0:
        print(f'down {n}', flush=True)
        time.sleep(1)
        yield
        n -= 1


def countup(stop):
    x = 0
    while x < stop:
        print(f'up {x}', flush=True)
        time.sleep(1)
        yield
        x += 1


async def await_countdown(n):
    while n > 0:
        print(f'down {n}', flush=True)
        await scheduler.sleep(4)
        n -= 1


async def await_countup(stop):
    x = 0
    while x < stop:
        print(f'up {x}', flush=True)
        await scheduler.sleep(1)
        x += 1