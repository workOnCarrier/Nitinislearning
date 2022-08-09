
# threaded target
from queue import Queue
from threading import Thread

from utube_trials.DavidBeazley_generators.building_blocks import coroutine


@coroutine
def threaded(target):
    messages = Queue()
    def run_target():
        while True:
            item = messages.get()
            if item is GeneratorExit:
                target.close()
                return
            else:
                target.send(item)
    Thread(target=run_target()).start()
    try:
        while True:
            item = yield
            messages.put(item)
    except GeneratorExit as ex:
        messages.put(ex)