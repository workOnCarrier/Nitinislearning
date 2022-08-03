class Countdown:
    def __init__(self, start):
        self.count = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count = r - 1
        return r


#  this is ssame as

def gen_countdown(start):
    while start > 0:
        yield start
        start -= 1


def use_class_generator_countdown(start):
    counter = Countdown(start)
    for num in counter:
        print(f' from class generator {num}')


def use_function_generator_countdown(start):
    for num in gen_countdown(start):
        print(f' from function generator {num}')


def play_generator_expressions():
    a = [1, 2, 3, 4]
    b = (2 * x for x in a)  # generates a generator object
    c = [2 * x for x in a]  # generates a list
    for i in b:
        print(f"values from b {i}")   # prints values
    else:
        print("first run of for loop for b ends")
    for i in b:
        print(f'values from b {i}')  # does not print as generator has been consumed
    else:
        print(f" second run of for loop for b ends")

    for i in c:
        print(f"values from c {i}")   # prints values
    else:
        print("first run of for loop for c ends")
    for i in c:
        print(f'values from c {i}')  # print as c is a list obtained from generator saved
    else:
        print(f" second run of for loop for c ends")


if __name__ == "__main__":
    start = 5
    use_class_generator_countdown(start)
    use_function_generator_countdown(start)
    play_generator_expressions()
