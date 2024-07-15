s = input("camelCase: ")
snake = ""

for ch in s:
    if ch.isupper():
        snake += "_" + ch.lower()
    else:
        snake += ch

print("snake_case:", snake)