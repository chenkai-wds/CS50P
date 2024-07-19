def main():
    percentage = convert(input("Fraction: "))
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x, y = fraction.strip().split('/')
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            return round(x / y * 100)
        except (ZeroDivisionError, ValueError):
            pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
