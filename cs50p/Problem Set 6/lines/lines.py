import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

if sys.argv[1][-3:] != '.py':
    sys.exit('Not a Python file')

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit('File does not exist')

counter = 0
for line in file:
    line = line.strip()
    if line.startswith('#') or not line:
        continue
    else:
        counter += 1

file.close()
print(counter)
