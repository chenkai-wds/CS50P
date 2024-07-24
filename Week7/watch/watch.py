import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    search = re.search(r"^.*src=\"https?://(www\.)?youtube.com/embed/([^\"]+)\".*></iframe>$", s)
    if search:
        return f"https://youtu.be/{search.group(2)}"
    else:
        return "None"


if __name__ == "__main__":
    main()

"""
# another way

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.match(
        r'<iframe.*?src="(https?:\/\/(?:www\.)?youtube\.com(?:\/embed)?\/[a-zA-z0-9_-]+)".*?',
        s,
    ):
        url = match.group(1).split("/")[-1]
        return f"https://youtu.be/{url}"
    return None


if __name__ == "__main__":
    main()
"""