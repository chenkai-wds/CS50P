from PIL import Image, ImageOps
import sys

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

input = sys.argv[1]
output = sys.argv[2]
types = (".jpg", ".jpeg", ".png")

if not input.endswith(types) or not output.endswith(types):
    print("Invalid input")
    sys.exit(1)
elif input.split(".")[1] != output.split(".")[1]:
    print("Input and output have different extensions")
    sys.exit(1)
else:
    shirt = Image.open("shirt.png")
    try:
        with Image.open(input) as im:
            im = ImageOps.fit(im, shirt.size)
            im.paste(shirt, shirt)
            im.save(output)
    except FileNotFoundError:
        sys.exit("File does not exist.")
