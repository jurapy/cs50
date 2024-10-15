import csv
import sys


def main():

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:
        print("Invalid arguments")

    # TODO: Read database file into a variable

    lista = []

    with open(sys.argv[1]) as database:
        dictReader = csv.DictReader(database)

        for row in dictReader:
            lista.append(row)

    # TODO: Read DNA sequence file into a variable

    seq = ''

    with open(sys.argv[2], 'r') as dnafile:
        reader = csv.reader(dnafile)

        for row in reader:
            for char in row:
                seq += char

    # TODO: Find longest match of each STR in DNA sequence

    listsrt = []

    with open('databases/small.csv') as database2:
        subseqs = csv.reader(database2)

        first_row = next(subseqs)  # Get the first row

        for srt in range(1, len(first_row)):
            counter = longest_match(seq, first_row[srt])
            listsrt.append({first_row[srt] : counter})

    # TODO: Check database for matching profiles

    newdict = {}

    pronaden_element = None

    for element in lista:
        if all(element[kljuc] == str(vrijednost) for kljuc, vrijednost in newdict.items()):
            pronaden_element = element
            break


    if pronaden_element == None:
        print('No match')
    else:
        print(pronaden_element['name'])

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
