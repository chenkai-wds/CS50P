import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    f = sys.argv[1]
    if not f.endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
    try:
        with open(f, "r") as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if line.strip() != "" and not line.strip().startswith("#"):
                    count += 1
            print(f"{count}")
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
