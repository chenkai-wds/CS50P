def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    digit = False
    for i in range(len(s)):
        if i <= 1 and not s[i].isalpha():
            return False
        if not s[i].isalpha() and not s[i].isdigit():
            return False
        if not digit and [i].isdigit() :
            if s[i] == '0':
                return False
            else:
                digit = True
        if digit and s[i].isalpha():
            return False
    return True

if __name__ == "__main__":
    main()