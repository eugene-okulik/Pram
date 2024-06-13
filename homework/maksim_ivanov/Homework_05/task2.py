nums = (
    'результат операции: 42',
    'результат операции: 514',
    'результат работы программы: 9'
)

for num in nums:
    result = int(num[num.index(':')+2:]) + 10
    print(result)
