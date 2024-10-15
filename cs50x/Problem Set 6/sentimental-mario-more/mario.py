# TODO
from cs50 import get_int

while True:
    height = get_int('Height: ')
    if height > 0 and height < 9:
        break

one = 1

for n in range(height):
    print(' ' * (height-1), end='')
    print('#' * one, end='')
    print('  ', end='')
    print('#' * one, end='')
    height -= 1
    one += 1
    print()
