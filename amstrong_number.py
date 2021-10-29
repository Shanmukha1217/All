import common as c

def main():
    num = int(input('enter a num: '))
    if is_amstrong(num):
         return print(f'{num} is a amstrong')
    return print(f'{num} is not amstrong')


def is_amstrong(num:int)-> bool:
    if result(num) == num:
        return True
    return False


def no_of_digits(num:int)->int:
    count = 0
    while num:
        num = c.num_truncate(num)
        count = c.add(count, 1)
    return count


def result(num:int)-> int:
    temp = num
    res = 0
    while temp:
        last_digit = c.digit_retriever(temp)
        res =c.add(res, (last_digit ** no_of_digits(num)))
        temp = c.num_truncate(temp)
    return res


if __name__ == "__main__":
    main()