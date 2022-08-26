smallest_positive = 2520
x = 0
yes = True
all_numbers = True

while yes:
    for i in range(3, 21):
        if smallest_positive % i == 0:
            all_numbers = True
            x += 1
        else:
            all_numbers = False
            break

    if all_numbers:
        print(smallest_positive)
        yes = False

    all_numbers = True

    smallest_positive += 2
