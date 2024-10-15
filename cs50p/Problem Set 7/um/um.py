import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r'(^|\W)um([ ,\.!\?]|$)'
    #mozes i korsititi (U|u) ali htio sam isprobati flags
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
