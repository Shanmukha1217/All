import common as c


def main():
    num = c.read('enter the number: ')
    if is_palindrome(num):
        print(f'{num} is palindrome')
    else:
        print(f'{num} is not palindrome')


def is_palindrome(num):
    if num == result(num):
        return True
    return False

def result(num):
    temp = num
    res = int()
    while temp:
        last_digit =c.digit_retriever(temp)
        res = c.add((res*10) ,last_digit)
        temp = c.num_truncate(temp)
    print(res)
    return res

if __name__ == '__main__':
    main()