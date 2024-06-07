a = 10
b = 5


def area_triangle(a, b):
    return a*b/2


def hypotenuse(a, b):
    return (a**2 + b**2)**(1/2)


print(f'Катеты прямоугольного треугольника равны {a} и {b}\n'
      f'Гипотенуза треугольника = {hypotenuse(a, b)}\n'
      f'Площадь треугольника = {area_triangle(a, b)}')
