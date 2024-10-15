nameslist = []

while True:
    try:
        name = input('Name: ')
    except EOFError:
        print()
        break
    else:
        nameslist.append(name)

print('Adieu, adieu, to ', end='')

if len(nameslist) > 1:
    nameslist[-1] = 'and ' + nameslist[-1]

    for name in nameslist[:-1]:
        if len(nameslist) > 2:
            print(name, end=', ')
        else:
            print(name, end=' ')
print(nameslist[-1])
