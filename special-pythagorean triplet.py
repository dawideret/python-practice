import math

out = False

while not out:
    for a in range(500):
        for b in range(500):
            d = (a ** 2) + (b ** 2)
            c = math.sqrt(d)
            e = a * b * c
            f = a + b + c

            if f == 1000:
                print(e)
                out = True
