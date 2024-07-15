s = input("Input: ")
o = ""
for ch in s:
    if ch not in "aeiouAEIOU":
        o += ch
print("Output:",  o)

"""
# another way
s = input("Input: ")

ans = "".join([ch for ch in s if ch.lower() not in "aeiou"])
print("Output:", ans)

"""