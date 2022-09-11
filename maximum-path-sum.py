pyramid = [
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [88, 2, 77, 73, 7, 63, 67],
    [19, 1, 23, 75, 3, 34],
    [20, 4, 82, 47, 65],
    [18, 35, 87, 10],
    [17, 47, 82],
    [95, 64],
    [75]
]

start_point = [0, 2]
total = 0


def find_route(sat_point):  # sat_point is the starting point
    tot = 0

    opt_1 = [999, 999]
    opt_2 = [999, 999]
    opt_3 = [999, 999]
    opt_4 = [999, 999]
    opt_5 = [999, 999]
    opt_6 = [999, 999]
    opt_7 = [999, 999]
    opt_8 = [999, 999]
    opt_9 = [999, 999]
    opt_10 = [999, 999]
    opt_11 = [999, 999]
    opt_12 = [999, 999]

    # INDEX FIRST ( GREEN )
    if sat_point[1] == 0:
        opt_1[0] = 0
        opt_1[1] = 0

    # INDEX LAST ( BLUE )
    elif sat_point[1] == len(pyramid[sat_point[0]]) - 1:
        opt_2[0] = len(pyramid[sat_point[0]]) - 1
        opt_2[1] = len(pyramid[sat_point[0]]) - 1

    # INDEX +1 ( ORANGE )
    elif sat_point[1] == 1:
        opt_3[0] = 0
        opt_3[1] = 0
        opt_4[0] = 1
        opt_4[1] = 0
        opt_5[0] = 1
        opt_5[1] = 1

    # INDEX -1 ( YELLOW )
    elif sat_point[1] == len(pyramid[sat_point[0]]) - 2:
        opt_6[0] = len(pyramid[sat_point[0]]) - 2
        opt_6[1] = len(pyramid[sat_point[0]]) - 2
        opt_7[0] = len(pyramid[sat_point[0]]) - 2
        opt_7[1] = len(pyramid[sat_point[0]]) - 1
        opt_8[0] = len(pyramid[sat_point[0]]) - 1
        opt_8[1] = len(pyramid[sat_point[0]]) - 1

    # INDEX +2 or -2 and between ( RED )
    elif 2 <= sat_point[1] <= len(pyramid[sat_point[0]]) - 2:
        opt_9[0] = sat_point[1] - 1
        opt_9[1] = sat_point[1] - 2
        opt_10[0] = sat_point[1] - 1
        opt_10[1] = sat_point[1] - 1
        opt_11[0] = sat_point[1]
        opt_11[1] = sat_point[1] - 1
        opt_12[0] = sat_point[1]
        opt_12[1] = sat_point[1]

    # Calculations - Choosing the highest path
    options_to_check = [opt_1, opt_2, opt_3, opt_4, opt_5, opt_6, opt_7, opt_8, opt_9, opt_10, opt_11, opt_12]
    valid_options = []
    for option in options_to_check:
        if option[0] != 999:
            valid_options.append(option)
    print(valid_options)  # Visual Indicator
    # !!! Work on Checking which of the leftover paths is the best one !!!
    return 0


total += find_route(start_point)
