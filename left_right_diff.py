
def left(f, x, h):
    return (f(x) - f(x - h)) / h


def right(f, x, h):
    return (f(x + h) - f(x)) / h


def central(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def second(f, x, h):
    return (f(x - h) - 2*f(x) + f(x + h)) / (h**2)


