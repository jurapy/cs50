import pyfiglet
import random
import sys

fontlist = pyfiglet.Figlet().getFonts()

chosenfont = 'default'

if len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    if sys.argv[2] in fontlist:
        chosenfont = sys.argv[2]
    else:
        print('Not valid font')
        sys.exit(2)
elif len(sys.argv) == 1:
    chosenfont = random.choice(fontlist)
else:
    sys.exit(1)

text = input('text: ')
ftext = pyfiglet.figlet_format(text, font=chosenfont)
print(ftext)

