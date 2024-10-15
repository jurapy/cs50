import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    lista = []
    pattern = r'(\d?\d):?(\d\d)? (AM|PM) to (\d?\d):?(\d\d)? (AM|PM)'

    if matches := re.match(pattern, s):
        for i in range(1, 7):
            lista.append(matches[i])

        if lista[1] == None:
            lista[1] = 0
        if lista[4] == None:
            lista[4] = 0

        if int(lista[0]) > 12 or int(lista[3]) > 12:
            raise ValueError()
        if int(lista[1]) > 59 or int(lista[4]) > 59:
            raise ValueError()

        if lista[2] == 'PM' and lista[0] != '12':
            lista[0] = int(lista[0]) + 12
        elif lista[2] == 'AM' and int(lista[0]) == 12:
            lista[0] = '0'

        if lista[5] == 'PM' and lista[3] != '12':
            lista[3] = int(lista[3]) + 12
        elif lista[5] == 'AM' and int(lista[3]) == 12:
            lista[3] = '0'

        return f'{int(lista[0]):02}:{int(lista[1]):02} to {int(lista[3]):02}:{int(lista[4]):02}'

    else:
        raise ValueError()

if __name__ == "__main__":
    main()
