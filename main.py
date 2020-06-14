import sys


def main(arg):
    for i in range(arg):
        print(f"{i} {i**2}")


if __name__ == "__main__":
    arg = int(sys.argv[1])
    main(arg)
