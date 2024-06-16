number = 2
user_number = int(input('Угадай цифру: '))
while True:
    if number != user_number:
        user_number = int(input('Попробуйте снова: '))
        continue
    else:
        print('Поздравляю! Вы угадали!')
        break
