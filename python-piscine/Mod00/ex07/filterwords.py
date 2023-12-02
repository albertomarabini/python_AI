import sys

def reprint_s(ss, n):
    for s in ss.split():
        if len(s) > n:
            print(s)

def main():
    if len(sys.argv) != 3:
        print("ERROR")
        return
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("ERROR")
        return
    reprint_s(sys.argv[1], n)

if __name__ == "__main__":
    main()
