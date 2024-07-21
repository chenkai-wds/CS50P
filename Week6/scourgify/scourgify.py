import sys
import csv

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    try:
        with open(sys.argv[1]) as input, open(sys.argv[2], "w") as output:
            reader = csv.DictReader(input)
            writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last_name, first_name = row["name"].strip().split(", ")
                writer.writerow(
                    {"first": first_name, "last": last_name, "house": row["house"]}
                )

    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
