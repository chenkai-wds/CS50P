s = list()

while True:
    try:
        t = input("Name: ")
        s.append(t)
    except EOFError:
        break

text = "Adieu, adieu,"
for i in range(len(s)):
    if i == 0:
        text = text + " to " + s[0]
    elif i < len(s) - 1:
        text = text + " " + s[i]
    else:
        text = text + " and " + s[i]
    if i < len(s) - 1 and len(s) > 2:
        text += ","

print(f"{text}")

"""
another way:

import inflect

p = inflect.engine()
names = []
while True:
    try:
        names.append(input("Name: ").strip())
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(names)}")

"""