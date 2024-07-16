items = dict()
while True:
    try:
        item = input()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        print()
        break

for item in sorted(items):
    print(f"{items[item]} {item.upper()}")

"""
# another solution
list = {}
while True:
    try:
        item = input("").upper()
    except EOFError:
        print()
        break

    if item in list:
        list[item] += 1
    else:
        list[item] = 1

for item, cnt in sorted(list.items()):
    print(f"{cnt} {item}")

"""