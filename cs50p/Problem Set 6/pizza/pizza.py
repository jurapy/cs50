import sys

from csv import DictReader
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
if sys.argv[1][-4:] != '.csv':
    sys.exit('Not a CSV file')

pizzas = []

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit('File does not exist')
else:
    reader = DictReader(file)
    for row in reader:
        pizzas.append(row)

print(tabulate(pizzas, tablefmt='grid', headers='keys'))
