text = input('Expression: ')

x, y, z = text.split(' ')
x = float(x)
z = float(z)

if y == '+':
    print(x + z)
elif y == '-':
    print(x - z)
elif y == '*':
    print(x * z)
elif y == '/':
    print(x / z)
else:
    print('Not valid!')
