import random
import sys

def main():
    level = get_level()
    score = 0

    for question in range(1,11):
        print(f'question_counter: {question}')
        x = generate_integer(level)
        y = generate_integer(level)
        errors = 0
        z = -1

        try:
            z = int(input(f'{x} + {y} = '))
        except ValueError:
            pass

        while (x+y) != z:
            print('EEE')
            errors += 1
            if errors == 3:
                break
            try:
                z = int(input(f'{x} + {y} = '))
            except ValueError:
                pass

        if errors == 3:
            print(f'{x} + {y} = {x+y}')
            continue
        score += 1

    print(f'Score: {score}')
    sys.exit(0)


def get_level():
    level = 0
    while level < 1 or level > 3:
        try:
            level = int(input('Level: '))
        except ValueError:
            pass
    return level


# for some reason randrange doesn't work but randint does
def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
    else:
        x = random.randint(100,999)
    return x


if __name__ == "__main__":
    main()
