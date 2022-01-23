import queue
import time
import threading

from async_concurrent.operations import countdown, countup

# sequential
from async_concurrent.producer_consumer import producer, consumer

threading.Thread(target=countdown, args=(5,)).start()
threading.Thread(target=countup, args=(5,)).start()

q = queue.Queue()

threading.Thread(target=producer, args=(q, 20)).start()
threading.Thread(target=consumer, args=(q,)).start()
