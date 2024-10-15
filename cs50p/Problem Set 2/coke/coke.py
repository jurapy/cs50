coinsum = 0

print('Amount Due:', 50)

while(coinsum < 50):
    coins = int(input('Insert coin: '))

    if coins == 5 or coins == 10 or coins == 25:
        coinsum += coins

    change = coinsum - 50

    if coinsum < 50:
        print('Amount Due:', 50 - coinsum)

print('Change Owed:', change)
