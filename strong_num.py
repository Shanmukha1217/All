from math import factorial

def main():
    num = int(input('Enter the number: '))
    is_strong(num)


def is_strong(num):
    if result(num) == num:
        return print('is a strong number')
    return print('is not a strong number')


def result(num):
    res = 0
    while num:
        last_digit = num % 10
        res += factorial(last_digit)
        num //= 10
    return res


if __name__ == "__main__":
    main()


