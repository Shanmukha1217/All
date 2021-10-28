import strong_num


def is_strong(num)-> bool:
    if num ==strong_num.result(num):
        return True
    return False


def strong_serie(upper):
    count = int()
    num =1
    while count < upper:
        if is_strong(num):
            print(f'{num} is a strong number')
            count += 1
        num += 1
    print(count)

upper = int(input('Enter the upper limit: '))
strong_serie(upper)