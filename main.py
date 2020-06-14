import sys


def func(arg):
    for i in range(arg):
        print(f'{i} {i**3}')


arg = int(sys.argv[1])
func(arg)
