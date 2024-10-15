while True:
    try:
        fuel_level = input("Fraction: ")
        x, y = fuel_level.split(sep='/')
        x = int(x)
        y = int(y)
        if y == 0:
            continue
        if x > y:
            continue
        break

    except ValueError:
        pass

z = x / y * 100

if z >= 99:
    z = 'F'
    print(f'{z}')

elif z <= 1:
    z = 'E'
    print(f'{z}')

else:
    print(f'{z:.0f}%')

'''
import pytest

def main():
    fraction = input('Fraction: ')
    print(gauge(convert(fraction)))

def convert(fraction):
    x,y = fraction.split(sep='/')
    x = int(x)
    y = int(y)
    z = x / y
    if x > y:
        raise ValueError('X greater than Y')
    return int(round(z*100))

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'

if __name__ == "__main__":
    main()
'''
