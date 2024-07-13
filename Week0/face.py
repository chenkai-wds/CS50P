def convert(str1):
    return str1.replace(':)', '🙂').replace(':(', '🙁')

def main():
    print(convert(input()))

main()