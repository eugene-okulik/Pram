def decorator(func):
    def wrapper(first, second, operation=None):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation)
    return wrapper


@decorator
def calc(first, second, operation):
    print(f'{operation=}')
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


print(calc(3, 5, '+'))
print(calc(3, 3, '-'))
print(calc(-3, 5, '+'))
print(calc(6, 5, '+'))
