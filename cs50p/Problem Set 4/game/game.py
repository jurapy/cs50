import random

n = 0
while n < 2:
    try:
        n = int(input('Level: '))
    except ValueError:
        pass

rand = random.randrange(1, n)

guess = 0
while guess != rand:
    try:
        guess = int(input('Guess: '))
    except ValueError:
        pass
    else:
        if guess > rand:
            print('Too large!')
        elif guess < rand and guess > 0:
            print('Too small!')
        else:
            pass

print('Just right!')
