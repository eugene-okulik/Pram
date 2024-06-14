text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,'
        ' dignissim vitae libero')

result = []
words = text.split()
for word in words:
    if word[-1] not in ('.', ','):
        result.append(word + 'ing')
    else:
        result.append(word[:-1] + 'ing' + word[-1])
print(' '.join(result))
