from prime_num import is_prime


def main() :
    lower = int(input('Enter the lower range.\n'))
    upper = int(input('Enter the upper range.\n'))
    print(f'\nPrime numbers within the range ({lower},{upper}) are:')
    for i in range(lower, upper) :
        if is_prime(i) :
            print(f'{i}')

        
if __name__ == '__main__' :
    main()