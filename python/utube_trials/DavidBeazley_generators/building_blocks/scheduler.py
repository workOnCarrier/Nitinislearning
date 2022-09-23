from queue import Queue

from utube_trials.DavidBeazley_generators.building_blocks.task import Task, SystemCall


class GetTid(SystemCall):
    def handle(self):
        self.task.send_val = self.task.tid
        self.sched.schedule(self.task)


class Scheduler:
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}

    def new(self, target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def schedule(self, task):
        self.ready.put(task)

    def exit(self, task: Task):
        del self.taskmap[task.tid]

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
                if isinstance(result, SystemCall):
                    result.task = task
                    result.sched = self
                    result.handle()
                    continue
            except StopIteration as ex:
                self.exit(task)
                continue
            self.schedule(task)
