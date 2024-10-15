import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_regex = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    if match := re.match(ip_regex, ip):
        for element in match.groups():
            if 0 <= int(element) <= 255:
                pass
            else:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
