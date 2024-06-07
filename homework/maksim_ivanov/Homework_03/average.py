x = 26
y = 150


def average(a, b):
    return (a + b) / 2


def geometric_mean(a, b):
    return (a * b) ** (1/2)


print(f'Среднее арифметическое {x} и {y} = {average(x, y)}\n'
      f'Среднее геометрическое {x} и {y} = {geometric_mean(x, y)}')
