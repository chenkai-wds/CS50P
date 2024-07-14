def interpret(x, y, z):
    match y:
        case '+':
            return float(x) + float(z)
        case '-':
            return float(x) - float(z)
        case '*':
            return float(x) * float(z)
        case '/':
            return float(x) / float(z)

def main():
    x, y, z = input("Expression: ").split()
    ans = interpret(x, y, z)
    print(f"{ans:.1f}")

if __name__ == "__main__":
    main()