import sys


def main(arg):
    for i in range(arg):
        print(str(i) + ' ' + str(i * i))


if __name__ == "__main__":
    arg = int(sys.argv[1])
    main(arg)
