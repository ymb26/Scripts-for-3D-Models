x1 = [0.000, -5.500, 6.000 ]
x2 = [0.000, -4.500, 6.000 ]
x3 = [2.500, -5.500, 6.000 ]
x4 = [2.500, -4.500, 6.000 ]
x5 = [5.000, -5.500, 6.000 ]
x6 = [5.000, -4.500, 6.000 ]
x7 = [7.500, -5.500, 6.000 ]
x8 = [7.500, -4.500, 6.000 ]
x9 = [10.000, -5.000, 6.000]
x10 = [0.000, 4.500, 6.000]
x11 = [0.000, 5.500, 6.000]
x12 = [2.500, 4.500, 6.000]
x13 = [2.500, 5.500, 6.000]
x14 = [5.000, 4.500, 6.000]
x15 = [5.000, 5.500, 6.000]
x16 = [7.500, 4.500, 6.000]
x17 = [7.500, 5.500, 6.000]
x18 = [10.000, 5.000, 6.000]


x0 = [0, 0, 0]
list_x_0 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18]
list_x_1 = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
list_x_2 = [x10, x11, x12, x13, x14, x15, x16, x17, x18]

for x in list_x_0:
    x0[0] += x[0]

print(x0)


