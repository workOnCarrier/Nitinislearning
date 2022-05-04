from functools import wraps, partial


def print_function_name(fn=None, *, prefix=''):
    # fn is function to be wrapped
    if fn is None:
        return partial(print_function_name, prefix=prefix)

    msg = prefix + fn.__qualname__

    @wraps(fn)
    def printer(*args, **kwargs):
        print(msg, end="\t")
        return fn(*args, **kwargs)

    return printer


@print_function_name
def add(a, b):
    # add two numbers
    return a + b


@print_function_name(prefix="--->")
def sub(a, b):
    # add two numbers
    return a + b

def print_methods(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, print_function_name(val))
    return cls

@print_methods
class ToBeDecorated():
    def a(self):
        print("having fun")
    def b(self):
        print("not having fun")

def play_method_print():
    s = ToBeDecorated()
    s.a()
    s.a
    s.b()
    s.b



def play_decorated_add():
    value = add(3, 4)
    print(value)
    value = sub(4,3)
    print (value)


if __name__ == '__main__':
    # play_decorated_add()
    play_method_print()
