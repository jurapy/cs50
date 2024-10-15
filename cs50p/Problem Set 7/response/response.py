from validator_collection import checkers


if checkers.is_email(input("What's your email address? ")):
    print('Valid')
else:
    print('Invalid')
