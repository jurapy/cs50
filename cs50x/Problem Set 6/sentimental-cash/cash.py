# TODO
from cs50 import get_float

def main():

    while True:
        dollars = get_float("How many dollars: ")
        if dollars >= 0:
            break

    cents = dollars * 100

    quarters = quartersFunction(cents)
    if quarters != 0:
        cents = cents % (quarters * 25)

    dimes = int(cents / 10)
    if dimes != 0:
        cents = cents % (dimes * 10)

    nickels = int(cents / 5)
    if nickels != 0:
        cents = cents % (nickels * 5)

    pennies = int(cents / 1)

    sum = quarters + dimes + nickels + pennies
    print(sum)

def quartersFunction(cents):
    cents /= 25
    return int(cents)

if __name__ == "__main__":
    main()
