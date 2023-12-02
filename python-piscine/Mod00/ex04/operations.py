import sys

def perform_operations(a, b):
    print(f"Sum: {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product: {a * b}")

    # Handling division and modulo operations with error checking
    try:
        print(f"Quotient: {a / b}")
    except ZeroDivisionError:
        print("Error: Division by zero")

    try:
        print(f"Remainder: {a % b}")
    except ZeroDivisionError:
        print("Error: Modulo by zero")

def main():
    if len(sys.argv) == 3:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            perform_operations(a, b)
        except ValueError:
            print("Error: Both arguments must be integers")
    else:
        print("Usage: python3 script.py <integer A> <integer B>")

if __name__ == "__main__":
    main()
