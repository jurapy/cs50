def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0:2].isalpha() == False:
        return False

    for char in s:
        if char.isalpha() == False and char.isdigit() == False:
            return False

    prvibroj = 0
    for char in s:
        if char.isdigit():
            prvibroj += 1
        if char == '0' and prvibroj == 1:
            return False

    zadnji = len(s) - 1
    if s[zadnji].isalpha() and prvibroj > 0:
        return False

    for i in range(1, len(s)):
        if s[i].isalpha() and s[i-1].isdigit():
            return False
    return True

if __name__ == '__main__':
    main()
