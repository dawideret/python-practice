import math

x = str(int(math.pow(2, 1000)))
y = 0

for digit in x:
    y += int(digit)

print(y)
