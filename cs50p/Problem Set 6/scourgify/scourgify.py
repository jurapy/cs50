import csv
import sys

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

buffer = []

try:
    beforefile = open(sys.argv[1])
except FileNotFoundError:
    sys.exit('Could not read invalid_file.csv')
else:
    reader = csv.DictReader(beforefile)
    for row in reader:
        last, first = row['name'].split(sep=', ')
        buffer.append({'first':first, 'last':last, 'house':row['house']})
    beforefile.close()

with open(sys.argv[2], 'w') as afterfile:
    writer = csv.DictWriter(afterfile, fieldnames=['first','last','house'])
    writer.writeheader()

    for element in buffer:
        writer.writerow({
            'first':element['first'],
            'last':element['last'],
            'house':element['house']
            })
