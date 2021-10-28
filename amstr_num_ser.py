import amstrong_number


def amstrong_series() :
    num = int(input('Enter the number of amstrong numbers: '))
    count = 0
    n = 1
    while count < num :
        if amstrong_number.is_amstrong(n):
            print(f'{n} is amstrong number')
            count += 1
        n += 1


amstrong_series()