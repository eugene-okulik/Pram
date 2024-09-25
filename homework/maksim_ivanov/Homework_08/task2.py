import sys

sys.set_int_max_str_digits(100000)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci()
for i in range(1, 100001):
    num = next(fib_gen)
    if i in [5, 200, 1000, 100000]:
        print(f'{i}-ое число последовательности Фибонначи: {num}')
