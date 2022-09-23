from utube_trials.DavidBeazley_generators.building_blocks.scheduler import Scheduler, GetTid
from utube_trials.DavidBeazley_generators.building_blocks.task import Task


def play_dummy_tasks():
    def foo():
        print("running part 1")
        yield
        print("running part 2")
        yield
        print("running part 3")

    t1 = Task(foo())
    print(f"running foo")
    t1.run()
    print(f"resuming foo")
    t1.run()
    print(f"resuming again foo")
    t1.run()


def play_scheduler_dummy_tasks():
    def foo():
        mytid = yield GetTid()
        for instance in range(5):
            print(f'I am foo {instance} for {mytid}')
            yield
    def bar():
        mytid = yield GetTid()
        for instance in range(8):
            print(f'I am bar {instance} for {mytid}')
            yield
    sched = Scheduler()
    sched.new(foo())
    sched.new(bar())
    sched.mainloop()

if __name__ == "__main__":
    # play_dummy_tasks()
    play_scheduler_dummy_tasks()
