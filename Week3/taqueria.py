menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0
    while True:
        try:
            x = input("Item: ")
            x = x.title()
            total += menu[x]
            print(f"Total: ${total:.2f}")
        except KeyError:
            pass
        except EOFError:
            print()
            return

if __name__ == "__main__":
    main()

"""
another way
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

total = 0
while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")
    except EOFError:
        print()
        break
"""