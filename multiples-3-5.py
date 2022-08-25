x = 1000
y = 1
z = 0

while y < x:
    if y % 3 == 0 or y % 5 == 0:
        z += y
    y += 1

print(z)
