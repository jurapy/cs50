from cs50 import get_int
from math import ceil

def main():
    cardNum = get_int('Input card number: ')
    cardNum = str(cardNum)
    lenght = len(cardNum)
    if algorithm(cardNum):
        if lenght == 13 or lenght == 16 and cardNum[0] == '4':
            print('VISA')
        elif lenght == 15 and cardNum[0] == '3' and (cardNum[1] == '4' or cardNum[1] == '7'):
            print('AMEX')
        elif lenght == 16 and cardNum[0] == '5' and (cardNum[1] in '12345'):
            print('MASTERCARD')
        else:
            print('INVALID')
    else:
        print('INVALID')

def algorithm(cardNum):
    i = 2
    j = 1
    n = int(len(cardNum) / 2)
    secondN = ceil(len(cardNum) / 2)
    sum = 0

    for x in range(n):
        rest = 0
        penultimate = cardNum[len(cardNum) -i]
        luhn = int(penultimate) * 2
        if luhn > 9:
            rest = luhn % 10
            luhn = 1
        sum += luhn + rest
        i += 2

    for y in range(secondN):
        last = cardNum[len(cardNum) -j]
        sum += int(last)
        j += 2

    if sum % 10 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
