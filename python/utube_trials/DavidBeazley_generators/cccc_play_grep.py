from utube_trials.DavidBeazley_generators.building_blocks import coroutine


@coroutine
def mygrep(pattern):
    print(f"looking for {pattern}")
    while True:
        line = yield
        if pattern in line:
            print(line)


def play_with_mygrep():
    cr = mygrep("fun")
    cr.send("is python fun")  # prints the value
    cr.send("python is boring")  # does not print this


@coroutine
def my_grep_with_try_catch(pattern):
    print(f"looking for {pattern}")
    while True:
        try:
            line = yield
            if pattern in line:
                print(line)
        except Exception as ex:
            print(f"received exception {ex}")
            break


def play_with_my_grep_with_try_catch():
    cr = my_grep_with_try_catch("fun")
    cr.send("is python fun")  # prints the value
    cr.send("python is boring")  # does not print this
    cr.throw(RuntimeError, "trail exception")
    cr.close()
    cr.send(" python coroutine not running")


if __name__ == "__main__":
    # play_with_mygrep()
    play_with_my_grep_with_try_catch()
