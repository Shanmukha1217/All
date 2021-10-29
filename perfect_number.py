import common as c
def main():
    num = c.read('Enter the number: ')
    if is_perfect(num):
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not perfect number')


def is_perfect(num):
    if num == result(num):
        return True
    return False


def result(num):
    sum = 0
    for n in range(1, num):
        if num % n == 0:
            sum = c.add(sum, n)
    return sum 


if __name__ == "__main__":
    main()
