text = input('text: ')

text = text.lower().strip()

if text == '42' or text == 'forty-two' or text == 'forty two':
    print('yes')

else:
    print('no')
