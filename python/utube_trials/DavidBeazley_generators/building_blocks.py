def coroutine(func: callable):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return start
