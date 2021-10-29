import common as c
from reversenum import reverse


def main():
    lower = c.read('enter the lower range: ')
    upper = c.read('enter the upper range: ')   
    for i in range(lower, upper + 1):
        print(f'reverse of {i} is {reverse(i)}')


if __name__ == "__main__":
    main()