def repeat_me(func):
    def wrapper(text, count=1):
        for i in range(0, count):
            func(text, count)
    return wrapper


@repeat_me
def example(text, count=1):
    print(text)


example('print me', count=3)
