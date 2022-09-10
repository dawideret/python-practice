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

pointer_a = [0, 0]
pointer_b = [0, 0]
pointer_c = [0, 0]
total = 0


def find_route():
    point_a = pointer_a
    point_b = pointer_b
    point_c = pointer_c
    option_a_col = 0
    option_b_col = 0
    option_a1_col = 0
    option_a2_col = 0
    option_b1_col = 0
    option_b2_col = 0
    predicted_total = 0

    # Handling Rows Position
    if point_a[0] + 1 < len(pyramid):
        point_b[0] = point_a[0] + 1
        print("Test 00")
    else:
        point_b = point_a
        print("Test 01")
    if point_a[0] + 2 < len(pyramid):
        point_c[0] = point_a[0] + 2
        print("Test 02")
    else:
        point_c = point_a
        print("Test 03")

    if point_a == (point_b and point_c):
        print("Test 04")
        return 0  # Remember to address this.

    # Handling Columns Position
    if point_a[1] == 0:
        print("Test 05")
        option_a_col = point_a[1]
        option_b_col = point_a[1]

    elif point_a[1] == len(pyramid[point_a[0]]) - 1:
        print("Test 06")
        option_a_col = point_a[1] - 1
        option_b_col = point_a[1] - 2

    else:
        print("Test 07")
        option_a_col = point_a[1]
        option_b_col = point_a[1] - 1
        option_a1_col = point_a[1]
        option_a2_col = point_a[1] - 1
        option_b1_col = point_a[1]
        option_b2_col = point_a[1] - 1

    # Calculating Highest Route
    ret = 0

    if pyramid[point_a[0]][point_a[1]] + pyramid[option_a_col[0]][option_a_col[1]] # Continue From Here

find_route()
