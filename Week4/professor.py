import random

def main():
    level = get_level()
    countV = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        countE = 0
        while countE < 3:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans != x + y:
                    print("EEE")
                    countE += 1
                else:
                    countV += 1
                    break
            except ValueError:
                print("EEE")
                countE += 1
        if countE == 3:
            print(f"{x} + {y} = {x + y}")
    print("Score:", countV)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10 ** (level - 1), 10 ** level - 1)

if __name__ == "__main__":
    main()