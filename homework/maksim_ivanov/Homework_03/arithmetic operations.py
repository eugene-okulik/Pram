a = 10
b = 3


def summ(a1, a2):
    return a1 + a2


def difference(a1, a2):
    return a1 - a2


def multiplication(a1, a2):
    return a1 * a2


print(f'{a} + {b} = {summ(a, b)}\n'
      f'{a} - {b} = {difference(a, b)}\n'
      f'{a} * {b} = {multiplication(a, b)}')
