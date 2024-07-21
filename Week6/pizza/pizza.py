import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    f = sys.argv[1]
    if not f.endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    try:
        with open(f) as file:
            print(tabulate(csv.DictReader(file), headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
