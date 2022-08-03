def spam_v1():
    print("primed")
    while True:
        item = yield
        print("Got:", item)


def work_with_spam_1():
    s = spam_v1()
    print(s)  # expected to get a generator object
    print("generator not primed, priming")
    print(next(s))  # prints None -- advances execution to yield statement

def spam_v2():
    print("primed")
    count = 0
    while True:
        item = yield count
        print("Got:", item)
        count = count + 1

def work_with_spam_2():
    print("starting work with spam 2")
    s = spam_v2()
    print(s)
    print("generator not primed, priming")
    next(s)
    yield_value = s.send("hey")
    print(yield_value)



if __name__ == "__main__":
    work_with_spam_1()
    work_with_spam_2()
