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
    predicted_total = 0

    # Handling Rows Position
    if point_a[0] + 1 < pyramid[len(pyramid)]:
        point_b[0] = point_a[0] + 1
    else:
        point_b = point_a
    if point_a[0] + 2 < pyramid[len(pyramid)]:
        point_c[0] = point_a[0] + 2
    else:
        point_c = point_a

    if point_a == (point_b and point_c):
        return 0  # Remember to address this.

    # Handling Columns Position
    if point_a[1] == 0:
        point_b[1] = point_a[1]
        

