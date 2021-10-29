from common import read
import index

def main():
    choice = read('Choose one !!1. Single output\n2. Series output.\n')
    if choice == 1:
        single_output()
    elif choice == 2:
        series_output()
    else:
        print('Invalid choice.')


def single_output():
    print('\nYou selected Single output pick one')
    choice= menu()
    index.single(choice)

def series_output():
    print('You selected Series output pick one')
    choice= menu()
    index.series(choice)

def menu()-> int:
    print('1. Prime number\n 2. Perfect number\n 3. Amstrong number\n 4. Automorphic number')
    return read('5. Reverse a number\n 6. Palindrome number\n 7. Strong number')


if __name__ == '__main__':
    main()
    while input('\nDo you wish to continue? (y/n)\n').lower() == 'y':
        main()