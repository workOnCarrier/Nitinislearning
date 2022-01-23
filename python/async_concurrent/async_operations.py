import time

# from async_concurrent.yield_scheduler import scheduler
from async_concurrent.callback_scheduler import sched


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
        await sched.sleep(4)
        n -= 1


async def await_countup(stop):
    x = 0
    while x < stop:
        print(f'up {x}', flush=True)
        await sched.sleep(1)
        x += 1