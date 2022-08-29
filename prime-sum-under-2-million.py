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

for n in range(1, 2000001):
    if is_prime(n):
        print(n)
        result += n
    n += 1

print(result)
