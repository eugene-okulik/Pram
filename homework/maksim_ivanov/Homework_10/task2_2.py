from functools import wraps


def repeat_me(count=1):
    def decorator(func):
        @wraps(func)
        def wrapper(text):
            for i in range(0, count):
                func(text)
        return wrapper
    return decorator


@repeat_me(5)
def example(text):
    print(text)


example('print me')
