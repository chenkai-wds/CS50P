import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    search = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if search:
        for s in search.groups():
            if int(s) > 255 or int(s) < 0:
                return False
        return True
    return False


if __name__ == "__main__":
    main()

"""
# another way

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return False
    for num in ip.split("."):
        if int(num) < 0 or int(num) > 255:
            return False
    return True


if __name__ == "__main__":
    main()
"""