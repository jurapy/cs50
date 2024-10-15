def main():
    text = input('greeting: ')
    print(f'${value(text)}')


def value(greeting):
    greeting = greeting.lower().lstrip()
    if greeting[:5] == 'hello':
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()
