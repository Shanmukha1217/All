from math import sqrt


def main() :
    num = int(input('Enter the number:'))
    if is_prime(num) :
        print(f'{num} is prime.')
    else :
        print(f'{num} is n0t prime.')


def is_prime(num:int)->bool :
    if count_of_factors(num) :
        return False
    return True


def count_of_factors(num:int)->int :
    for i in range(2, int(sqrt(num))+1) :
        if num % i == 0:
            return 1
    return 0


if __name__ == '__main__' :
    main()