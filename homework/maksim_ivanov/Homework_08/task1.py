import random

salary = int(input("Введите зарплату:"))
bonus = 0
is_bonus = random.choice([True, False])
if is_bonus:
    bonus = random.randint(0, 50000)
print(f'{salary}, {is_bonus} - ${salary + bonus}')
