from async_concurrent import async_operations
from async_concurrent.operations import countdown_sched_callback, countup_sched_callback, \
    countup_sched_callback_
from async_concurrent.producer_consumer import callback_producer, callback_consumer, \
    async_producer, async_consumer
from async_concurrent.async_common import AsyncCallbackQueue, AsyncAwaitQueue
from async_concurrent.callback_scheduler import sched

# sched.call_soon(lambda: countdown_sched_callback(5))
# sched.call_soon(lambda: countup_sched_callback(5))
# sched.call_soon(lambda: countup_sched_callback_(21))
# sched.run()

# q = AsyncCallbackQueue()
# sched.call_soon(lambda: sched_producer(q, 10))
# sched.call_soon(lambda: sched_consumer('1', q))
# sched.call_soon(lambda: sched_consumer('2', q))
# sched.run()
# from async_concurrent.yield_scheduler import sched as scheduler

# scheduler.new_task(asyn_operations.countdown(5))
# scheduler.new_task(asyn_operations.countup(5))

# scheduler.new_task(asyn_operations.await_countdown(5))
# scheduler.new_task(asyn_operations.await_countup(21))
# scheduler.run()

# async_await_queue = AsyncAwaitQueue()
# scheduler.new_task(async_producer(async_await_queue, 10))
# scheduler.new_task(async_consumer(async_await_queue))
# scheduler.new_task(async_consumer(async_await_queue))
# scheduler.run()

q = AsyncCallbackQueue()
sched.call_soon(lambda: callback_producer(q, 10))
sched.call_soon(lambda: callback_consumer('1', q))
sched.call_soon(lambda: callback_consumer('2', q))
sched.new_task(async_operations.await_countdown(5))
sched.new_task(async_operations.await_countup(20))
sched.run()