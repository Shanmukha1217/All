import common as c
from palindrome import result

def main():
    lower = c.read('enter the lower range: ')
    upper = c.read('enter the upper range: ')
    for i in range(lower, upper + 1):
        if i == result(i):
            print(i)

if __name__ == "__main__":
    main()



