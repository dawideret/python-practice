def squares_of_first_100():
    x = 0

    for i in range(101):
        x += i ** 2
    return x


def square_of_sum_100():
    x = 0

    for i in range(101):
        x += i

    x **= 2
    return x


y = squares_of_first_100()
z = square_of_sum_100()

print(z - y)
