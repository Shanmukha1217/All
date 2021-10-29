import common as c


def main() :
    num = c.read('Enter a number.\n')
    if is_automorphic(num) :
        print(f'{num} is automorphic.')
    else:
        print(f'{num} isn\'t automorphic.')


def is_automorphic(num: int)->bool :
    square = num ** 2
    while num :
        if c.digit_retriever(num) != c.digit_retriever(square):
            return False
        num = c.num_truncate(num)
        squared = c.num_truncate(square)
    return True


if __name__ == '__main__':
    main()