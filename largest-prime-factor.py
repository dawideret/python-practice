our_number = 600851475143
increase = 2
counter = our_number
factors = []


while counter > 1:
    if counter % increase == 0:
        counter /= increase
        factors.append(counter)
    increase += 1

print(factors[-2])
