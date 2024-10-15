def main():
    text = input('Input: ')
    print(shorten(text))

def shorten(word):
    finished_word = ''

    for char in word:
        if char in 'AEIOUaeiou':
            continue
        else:
            finished_word += char
    return finished_word

if __name__ == "__main__":
    main()
