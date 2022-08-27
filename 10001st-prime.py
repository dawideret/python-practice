counter = 2
is_it_prime = 5
prime_list = [2, 3]

while counter < 10001:
    if is_it_prime % 2 != 0:
        for instance in prime_list:
            if is_it_prime % instance == 0:
                break
            elif instance == prime_list[-1]:
                prime_list.append(is_it_prime)
                print(prime_list[-1])
                counter += 1
                break
    is_it_prime += 2
