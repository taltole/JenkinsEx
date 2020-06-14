import sys
import urllib.request


def main():
    args = sys.argv[1:]
    urls = args[0].split(',')
    for url in urls:
        try:
            print(urllib.request.urlopen(url).read())
        except ValueError:
            print("Please provide valid urls")
            sys.exit(0)


if __name__ == '__main__':
    main()