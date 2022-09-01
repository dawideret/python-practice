def check_collatz(number):
    counter = 1

    while number != 1:
        if number % 2 == 0:
            number /= 2
            counter += 1
        else:
            number = number * 3 + 1
            counter += 1
    return counter


longest_starter = 1
longest_count = 1

for num in range(2, 1000001):
    count = check_collatz(num)
    if count > longest_count:
        longest_count = count
        longest_starter = num
        print(f"Longest Num: {longest_starter}, with count of: {longest_count}")
