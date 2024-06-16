nums = (
    'результат операции: 42',
    'результат операции: 514',
    'результат работы программы: 9',
    'результат: 2'
)


def plus_10(operation: str) -> int:
    return int(operation[operation.index(':') + 2:]) + 10


for num in nums:
    print(plus_10(num))
