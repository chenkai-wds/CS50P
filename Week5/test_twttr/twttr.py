def main():
    s = input("Input: ")
    print("Output:",  shorten(s))

def shorten(word):
    o = ""
    for ch in word:
        if ch not in "aeiouAEIOU":
            o += ch
    return o


if __name__ == "__main__":
    main()
