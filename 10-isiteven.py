def check(num):
    if num % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"

def main():
    n = int(input("Enter a number: "))
    result = check(n)
    print(result)

if __name__ == "__main__":
    main()