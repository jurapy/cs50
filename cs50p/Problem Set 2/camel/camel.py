name = input('name: ')

for char in name:
    if char.isupper():
        char = char.lower()
        print('_' + char, end='')
    else:
        print(char, end='')
print()
