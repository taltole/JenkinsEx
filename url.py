import sys
import urllib.request as ur


def main():
    args = sys.argv[1:]
    urls = args[0].split(',')
    for url in urls:
        try:
            with ur.urlopen(url) as response:
                html = response.read()
                print(html)
        except ValueError:
            print("Please provide valid urls")
            sys.exit(0)


if __name__ == '__main__':
    main()