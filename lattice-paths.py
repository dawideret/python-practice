import math
                    # Correct formula is:    (a + b)! / a! * b!
a = 20
b = 20

ab1 = math.factorial(a + b)

a2 = math.factorial(a)
b2 = math.factorial(b)

ab2 = a2 * b2

ab3 = ab1 / ab2

print(ab3)
