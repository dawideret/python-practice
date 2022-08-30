import math

natural_numbers = [1]
triangle_number = 1


def get_next_triangle():
    natural_numbers.append(natural_numbers[-1] + 1)
    global triangle_number
    triangle_number = 0
    for number in natural_numbers:
        triangle_number += number
    if triangle_number % 100 != 0:
        get_next_triangle()


def check_divisor_amount(number):
    divisor_amount = 0

    for i in range(2, int(math.floor(number + 1) / 2)):
        if number % i == 0:
            divisor_amount += 1

    return divisor_amount


while True:
    div_amount = check_divisor_amount(triangle_number)
    if div_amount >= 500:
        print("We Found it: ", triangle_number)
        break
    else:
        get_next_triangle()
        print(triangle_number, " - Div Amount: ", div_amount)
