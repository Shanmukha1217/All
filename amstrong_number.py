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
        num = truncate(num, 10)
        count = add(count, 1)
    return count


def result(num:int)-> int:
    temp = num
    res = 0
    while temp:
        last_digit = retrieve(temp, 10)
        res =add(res, (last_digit ** no_of_digits(num)))
        temp = truncate(temp, 10)
    return res

def add(num1, num2):
    return num1 + num2

def retrieve(num1, num2):
    return num1 % num2

def truncate(num1, num2):
    return num1 // num2



