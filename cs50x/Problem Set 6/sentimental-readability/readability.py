# TODO
from cs50 import get_string


def main():
    text = get_string('Text: ')

    lenght = len(text)

    words_counter = 0
    sentences_counter = 0
    letters_counter = 0
    #provjerit zasto u istom redu nemos imat vise varijabli i svima im dodjelit istu int vrijednost recimo 0

    for char in text:
        if char == ' ':
            pass
            words_counter += 1

        elif char in '.!?':
            sentences_counter += 1

        elif char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            letters_counter += 1

    words = words_counter + 1
    sentences = sentences_counter
    letters = letters_counter

    L = letters / words * 100
    S = sentences / words * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)
    #print(index)

    if index < 1:
        print('Before Grade 1')

    elif index >= 16:
        print('Grade 16+')

    else:
        print('Grade', index)

if __name__ == '__main__':
    main()