my_dict = {
    'tuple': (1, 3, 6, 8, 4, 7, 2),
    'list': [1, 2, 4, 5, 8, 9],
    'dict': {
        '1': (2, 'A'),
        '3': 3,
        4: [4, 7, 8],
        'xy': 'x1y1',
        5: 5,
        7: 111
    },
    'set': {1, 6, 5, 'A', 'Qwerty', 8}
}

for key, value in my_dict.items():
    if key == 'tuple':
        print('Последний элемент tuple: ' + str(value[-1]))
    elif key == 'list':
        value.append(22)
        value.pop(1)
    elif key == 'dict':
        value[("i am a tuple",)] = 'tuple'
        value.pop('3')
    elif key == 'set':
        value.add(56)
        value.remove(5)

print(my_dict)
