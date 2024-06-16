words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def many_words(words: dict) -> list:
    result = []
    for key, value in words.items():
        line = ''.join([key] * value)
        result.append(line)
    return result


for i in many_words(words):
    print(i)
