s = input("Greeting: ")
s = s.strip().lower()

if s.startswith("hello"):
    print("$0")
elif s[0] == 'h':
    print("$20")
else:
    print("$100")