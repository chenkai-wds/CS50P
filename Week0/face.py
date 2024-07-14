def convert(str):
    return str.replace(':)', '🙂').replace(':(', '🙁')

def main():
    print(convert(input()))

if __name__ == "__main__":
    main()