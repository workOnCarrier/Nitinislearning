import time

from async_concurrent.callback_scheduler import sched


def countdown(n):
    while n > 0:
        print(f'down {n}', flush=True)
        time.sleep(1)
        n -= 1


def countup(stop):
    x = 0
    while x < stop:
        print(f'up {x}', flush=True)
        time.sleep(1)
        x += 1


def countdown_sched_callback(n):
    if n > 0:
        print(f'down {n}', flush=True)
        # time.sleep(4)
        # sched.call_soon(lambda: countdown_sched_callback(n - 1))
        sched.call_later(4, lambda: countdown_sched_callback(n - 1))


def countup_sched_callback(stop, x=0):
    if x < stop:
        print(f'up {x}', flush=True)
        time.sleep(1)
        sched.call_soon(lambda: countup_sched_callback(stop, x + 1))


def countup_sched_callback_(stop):
    def _run(x):
        if x < stop:
            print(f'up {x}', flush=True)
            # time.sleep(1)
            # sched.call_soon(lambda: _run(x + 1))
            sched.call_later(1, lambda: _run(x+1))

    _run(0)
