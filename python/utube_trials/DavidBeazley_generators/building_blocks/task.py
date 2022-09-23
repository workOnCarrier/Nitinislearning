class Task(object):
    taskid = 0

    def __init__(self, target):
        Task.taskid += 1
        self.tid = Task.taskid
        self.target = target
        self.send_val = None

    def run(self):
        # if self.send_val:
        try:
            return self.target.send(self.send_val)
        except GeneratorExit as ex:
            print(f'finished with task {self.tid}')
            raise ex
        except StopIteration as ex:
            print(f'observed stop iteration for {self.tid}')
            raise ex


class SystemCall:
    def handle(self):
        pass
