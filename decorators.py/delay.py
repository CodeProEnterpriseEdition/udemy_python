from functools import wraps
from time import sleep


def delay(val):
    def inner(fn):
        @wraps(fn)
        def wrapper():
            print("Waiting {}s before running say_hi".format(val))
            sleep(val)
            return fn()
        return wrapper
    return inner


@delay(3)
def say_hi():
    print("say hi")


print(say_hi())


def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(timer, fn.__name__))
            sleep(timer)
            return fn(*args, **kwargs)
        return wrapper
    return inner


def say_hi():
    print("say hi")


print(say_hi())
