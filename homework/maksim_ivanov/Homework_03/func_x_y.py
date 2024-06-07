x = 16
y = 7


def func_x_y(x, y):
    return (x-y)/(1 + x*y)


print(f'{x=}, {y=}\n'
      f'({x}-{y})/(1+{x}*{y}) =  {func_x_y(x, y)}')