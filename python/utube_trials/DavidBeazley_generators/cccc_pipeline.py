# def source(target):
#     while not done:
#         item = produde_an_item()
#         target.send(item)
#     target.close()

# @coroutine
# def sink():
#     try:
#         while True:
#             item = yield
#     except GeneratorExit as ex:
#         pass
import sys
import time

from utube_trials.DavidBeazley_generators.building_blocks import coroutine


def follow(file_obj, target):
    file_obj.seek(0, 2)
    while True:
        line = file_obj.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


@coroutine
def printer():
    while True:
        line = yield
        print(line)


@coroutine
def my_filter(pattern, target):
    while True:
        line = yield
        if pattern in line:
            target.send(line)


if __name__ == "__main__":
    file_object = sys.stdin
    # follow(file_obj, printer())
    follow(file_object, my_filter("python", printer()))
