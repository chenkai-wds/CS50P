def get_fuel():
    while True:
        try:
            s = input("Fraction: ")
            x, y = s.strip().split('/')
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            return round(x / y * 100)
        except (ZeroDivisionError, ValueError):
            pass

def main():
    num = get_fuel()
    if num <= 1:
        print("E")
    elif num >= 99:
        print("F")
    else:
        print(f"{num}%")

if __name__ == "__main__":
    main()

"""
# another way
while True:
    try:
        x, y = map(int, input("Fraction: ").split("/"))
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        break
    except (ValueError, ZeroDivisionError):
        pass

percentage = round(x / y * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")

"""