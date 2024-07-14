def convert(str1):
    return str1.replace(':)', '🙂').replace(':(', '🙁')

def main():
    print(convert(input()))

if __name__ == "__main__":
    main()