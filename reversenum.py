import common as c
def main():
    num =c.read('enter the num: ')
    print(f'Reverse of {num} is {reverse(num)}.')


def reverse(num: int)-> int:
    res = int()
    while num:
        last_digit = c.digit_retriever(num)
        res = c.add((res*10) , last_digit)
        num = c.num_truncate(num)
    return res


if __name__ == '__main__':
    main()