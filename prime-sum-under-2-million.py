import math


def is_prime(num):
    if num <= 1:
        return False

    top = math.floor(math.sqrt(num)) + 1

    for i in range(2, top):
        if num % i == 0:
            return False

    return True


result = 0
n = 1
while n <= 2000000:
    if is_prime(n):
        print(n)
        result += n
    n += 2

print(result)
