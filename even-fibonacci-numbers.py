counter = 1
previous_values = [0, 1]
value_switch = 0
result = 0

while previous_values[0] + previous_values[1] < 4000000:
    counter = previous_values[0] + previous_values[1]
    previous_values[value_switch] = counter

    if value_switch == 0:
        value_switch = 1
    else:
        value_switch = 0

    if counter % 2 == 0:
        result += counter

print(result)
