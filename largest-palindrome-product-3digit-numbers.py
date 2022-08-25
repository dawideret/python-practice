result = 2003


def reverse_number(number):
    reversed_number = 0

    while number != 0:
        x = number % 10
        reversed_number = reversed_number * 10 + x
        number //= 10

    return reversed_number


first = 999
second = 999
num1 = 0
search = 0
finished_result = 0

while first > 0:
    while second > 0:
        num1 = first * second
        search = reverse_number(num1)
        if num1 == search and num1 > finished_result:
            finished_result = num1
        second -= 1
    second = 999
    first -= 1

print(finished_result)
