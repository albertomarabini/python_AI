import sys

def check_number(n):
    if n == 0:
        return "I'm Zero."
    elif n % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."

def main():
    if len(sys.argv) == 2:
        try:
            number = int(sys.argv[1])
            print(check_number(number))
        except ValueError:
            print("AssertionError: argument is not an integer")
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
    else:
        print("Usage: python3 whois.py <number>")

if __name__ == "__main__":
    main()