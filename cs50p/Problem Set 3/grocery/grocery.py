grocerylist = {}

while True:
    try:
        item = input().upper()

    except EOFError:
        print()

        sortlist = dict(sorted(grocerylist.items()))

        for artikl in sortlist:
            print(f'{sortlist[artikl]} {artikl}')
        break

    else:
        if item in grocerylist:
            grocerylist[item] += 1
        else:
            grocerylist.update({item:1})
