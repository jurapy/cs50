import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex_pattern = r'"https?://(?:www\.)?youtube\.com/embed/(\w+)"'
    if match := re.search(regex_pattern, s):
        result = 'https://youtu.be/' + match.group(1)
        return result



if __name__ == "__main__":
    main()
