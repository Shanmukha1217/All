from common import read
from automorphic_num import is_automorphic


def main():
    lower = read('Enter lower range: ')
    upper = read('Enter upper range: ')
    print(f'Automorphic numbers in range({lower}, {upper})')
    for i in range(lower, upper):
        if is_automorphic(i):
            print(f'{i}')
    print('Done.')


if __name__ == "__main__":
    main()