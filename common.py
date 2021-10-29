#simple function to add to number
def add(num1:int, num2:int):
    return num1 + num2


# truncate number by removing units place in the number
def num_truncate(num:int):
    return num // 10


def digit_retriever(num:int):
    return num % 10


#simply read user input
def read(msg: str)-> int:
    return int(input(msg))