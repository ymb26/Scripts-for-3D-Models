import math

i_max = 123
j_max = 145
k_max = 175
path = "C:\\Users\\Y_Baronov\\Desktop\\GIS\\PK1-8_str1_Насыщенность газом.map"
path_h = "C:\\Users\\Y_Baronov\\Desktop\\GIS\\PK1-8_str1_Глубина.map"


def make_array_search_last_z(i_max, j_max, k_max, path, x_cell, y_cell):
    composition = i_max * j_max * k_max
    super_list = []
    f = open(path, "r")
    l_file = [line.split() for line in f]
    general_list = []
    for line in l_file:
        general_list += line
    for g in general_list:
        element_of_list = str(g)
        if '*' not in element_of_list:
            super_list.append(element_of_list + ' ')
        elif element_of_list == '/':
            break;
        else:
            c = element_of_list[0:element_of_list.find('*')]
            d = element_of_list[element_of_list.find('*') + 1:]
            func = ''.join([d + ' ' for s in range(int(c))])
            super_list.append(func)
    str_super_list = ''.join(map(str, super_list))
    param1 = str_super_list.split()
    index = 0
    param = param1[len(param1) - composition - 1:]
    array_3d = [[[0 for i in range(i_max)] for j in range(j_max)] for k in range(k_max)]
    for k in range(k_max):
        for j in range(j_max):
            for i in range(i_max):
                if param[index] == '/':
                    break
                array_3d[k][j][i] = param[index]
                index = index + 1
    massive_of_z_saturation = []
    i = 0
    while array_3d[i][y_cell][x_cell] != '0':
        massive_of_z_saturation.append(array_3d[i][y_cell][x_cell])
        i += 1
    # print(param[i_max * 73 + 94])
    # print(array_3d[0][y_cell][x_cell])
    # print(array_3d[1][73][94])

    return len(massive_of_z_saturation)


def make_array_find_h_effective(i_max, j_max, k_max, path_h, z_last, x_cell, y_cell):
    Composition = i_max * j_max * k_max
    super_list = []
    f = open(path_h, "r")
    l_file = [line.split() for line in f]
    general_list = []
    for line in l_file:
        general_list += line
    for g in general_list:
        element_of_list = str(g)
        if '*' not in element_of_list:
            super_list.append(element_of_list + ' ')
        elif element_of_list == '/':
            break;
        else:
            c = element_of_list[0:element_of_list.find('*')]
            d = element_of_list[element_of_list.find('*') + 1:]
            func = ''.join([d + ' ' for s in range(int(c))])
            super_list.append(func)
    str_super_list = ''.join(map(str, super_list))
    param1 = str_super_list.split()
    index = 0
    param = param1[len(param1) - Composition - 1:]
    array_3d = [[[0 for i in range(i_max)] for j in range(j_max)] for k in range(k_max)]
    for k in range(k_max):
        for j in range(j_max):
            for i in range(i_max):
                if param[index] == '/':
                    break
                array_3d[k][j][i] = param[index]
                index = index + 1
    # print(float(array_3d[z_last - 1][y_cell][x_cell]) - float(array_3d[0][y_cell][x_cell]))
    return float(array_3d[z_last - 1][y_cell - 1][x_cell - 1]) - float(array_3d[0][y_cell - 1][x_cell - 1])


######


class my_well:
    def __init__(self, ix, iy, ix2, iy2, alpha, retreat, cell_value, length_well, h_effective):
        self.h_effective = h_effective
        self.cell_value = cell_value
        self.length_well = length_well
        self.alpha = alpha
        self.retreat = retreat
        self.ix = ix
        self.iy = iy
        self.ix2 = ix2 + retreat * math.cos(math.radians(alpha))
        self.iy2 = iy2 + retreat * math.sin(math.radians(alpha))

    def display_info(self):
        f.write("welltrack x\n")
        #f.writelines(self.ix, "\t", self.iy, "\t", 0, "\t", 0)
        #f.write(f"{self.ix}\t{self.iy}\t{0}\t{0}\n")
        #f.write('%d, %d, %d\n' % (self.ix, self.iy, 0))
        f.write('%d,\t %d,\t %d,\t %d\n' % (self.ix, self.iy, 0, 0))
        f.write('%d,\t %d,\t %d,\t %d\n' % (self.ix, self.iy, 500, 500))
        f.write('%d,\t %d,\t %d,\t %d\n' % (self.ix2, self.iy2, float(self.cell_value) + float(self.h_effective) / 3,
                                            ((float(self.cell_value) - 500) ** 2 + float(self.retreat) ** 2) ** 0.5 + 500))
        f.write('%d,\t %d,\t %d,\t %d' % (self.ix2 + self.length_well * math.cos(math.radians(self.alpha)),
                                            self.iy2 + self.length_well * math.sin(math.radians(self.alpha)),
                                            float(self.cell_value) + float(self.h_effective) / 3,
                                            ((float(self.cell_value) - 500) ** 2 + float(self.retreat) ** 2) ** 0.5 + 500 + 300))
        f.write('\t/\n')
        #print(self.ix, "\t", self.iy, "\t", 500, "\t", 500)
        #print(self.ix2, "\t", self.iy2, "\t", float(self.cell_value) + float(self.h_effective) / 3, "\t",
        #      ((float(self.cell_value) - 500) ** 2 + float(self.retreat) ** 2) ** 0.5 + 500)
        #print(self.ix2 + self.length_well * math.cos(math.radians(self.alpha)), "\t",
        #      self.iy2 + self.length_well * math.sin(math.radians(self.alpha)), "\t",
        #      float(self.cell_value) + float(self.h_effective) / 3, "\t",
        #      ((float(self.cell_value) - 500) ** 2 + float(self.retreat) ** 2) ** 0.5 + 500 + 300, "/")
        #print()


class third_point:
    def __init__(self, ix, iy, ix2, iy2, alpha, retreat):
        self.alpha = alpha
        self.retreat = retreat
        self.ix = ix
        self.iy = iy
        self.ix2 = ix2 + retreat * math.cos(math.radians(alpha))
        self.iy2 = iy2 + retreat * math.sin(math.radians(alpha))


# def find_cell(fslimi, fsxinc, map):


def read_file(map, i_max, j_max):
    path_xy_coordinates = "C:\\Users\\Y_Baronov\\Desktop\\GIS\\PK1-8_str1_Глубина_roof.cps"
    fslimi = []
    fsxinc = []
    array = []
    f = open(path_xy_coordinates, "r")
    l_file = [line.split() for line in f]
    for elem in l_file:
        array += elem
        if ("->Surface" in elem):
            array = []
        for minielem in elem:
            if minielem == "FSLIMI":
                fslimi += elem[1:]
            if minielem == "FSXINC":
                fsxinc += elem[1:]
    x_map_max = float(fslimi[1]) + (float(fsxinc[0]) / 2)
    y_map_min = float(fslimi[2]) - (float(fsxinc[0]) / 2)
    if map.ix2 % 100 < 50:
        x_cell = math.ceil((-map.ix2 + x_map_max + map.ix2 % 100) / float(fsxinc[0]))
    else:
        x_cell = math.ceil((-((map.ix2 - map.ix2 % 100) + 100) + x_map_max) / float(fsxinc[0]))
    if map.iy2 % 100 < 50:
        y_cell = math.ceil((map.iy2 - y_map_min - map.iy2 % 100) / float(fsxinc[0]))
    else:
        y_cell = math.ceil((((map.iy2 - map.iy2 % 100) + 100) - y_map_min) / float(fsxinc[0]))
    # print((i_max - x_cell) * j_max + y_cell - 1)
    # print("FINDDELL", x_cell, y_cell)
    # print(array[(i_max - x_cell) * j_max + y_cell - 1])
    return x_cell, y_cell, array[(i_max - x_cell) * j_max + y_cell - 1]
    # xy_cell = (i_max - x_cell) * j_max + y_cell - 1
    # print(x_cell, y_cell)
    # print(h_effective)
    # print(xy_cell)
    # print(array[xy_cell])
    # return array[xy_cell]


def find_cell_value(map1, i_max, j_max):
    x_cell, y_cell, array_value = read_file(map1, i_max, j_max)
    z_last = make_array_search_last_z(i_max, j_max, k_max, path, x_cell, y_cell)
    h_effective = make_array_find_h_effective(i_max, j_max, k_max, path_h, z_last, x_cell, y_cell)
    # print(read_file(map1, i_max, j_max))
    xy_cell = (i_max - x_cell) * j_max + y_cell - 1
    # print(xy_cell)
    # print(h_effective)
    # print(array_value)
    return array_value, h_effective


def well_result(ix, iy, ix2, iy2, alpha, retreat, length_well):
    map1 = third_point(ix, iy, ix2, iy2, alpha, retreat)
    array_value, h_effective = find_cell_value(map1, i_max, j_max)
    map = my_well(ix, iy, ix2, iy2, alpha, retreat, array_value, length_well, h_effective)
    map.display_info()

#def compdatmd(ix, iy, ix2, iy2, alpha, retreat, length_well):
 #   map1 = third_point(ix, iy, ix2, iy2, alpha, retreat)
  #  array_value, h_effective = find_cell_value(map1, i_max, j_max)
   # map = my_well(ix, iy, ix2, iy2, alpha, retreat, array_value, length_well, h_effective)

with open ( "C:\\Users\\Y_Baronov\\Desktop\\GIS\\wells.txt", 'w') as f:
    well_result(12604448.33, 7993175.934, 12604448.33, 7993175.934, 0, 500, 300)
    well_result(12604448.33, 7993175.934, 12604448.33, 7993175.934, 45, 500, 300)
    well_result(12604448.33, 7993175.934, 12604448.33, 7993175.934, 90, 500, 300)
    well_result(12604448.33, 7993175.934, 12604448.33, 7993175.934, 135, 500, 300)
    well_result(12604448.33, 7993175.934, 12604448.33, 7993175.934, 180, 500, 300)
    well_result(12604448.33, 7993175.934, 12604448.33, 7993175.934, 225, 500, 300)
    well_result(12604448.33, 7993175.934, 12604448.33, 7993175.934, 270, 500, 300)
    well_result(12604448.33, 7993175.934, 12604448.33, 7993175.934, 315, 500, 300)
    f.write('\n')
    f.write("WELSPECS\n")
    i = 0
    while i < 8:
        f.write("x")
        f. write('%d\t' % (i + 1))
        f.write(' \'\'\t')
        f.write('/\n')
        i += 1
    f.write('/\n')
    f.write('\n')
    i = 0
    f.write("COMPDATMD\n")
    while i < 8:
        f.write("x")
        f.write('%d\t' % (i + 1))
        f.write("\t1*\t\t1020\t\t1500\t\tMD\t3*\t0.168\t")
        f.write('/\n')
        i += 1
    f.write('/\n')

#print("---------------------------------------------------------------------------------------\n")
#well_result(12611029.85, 7994974.627, 12611029.85, 7994974.627, 0, 500, 300)
#well_result(12611029.85, 7994974.627, 12611029.85, 7994974.627, 45, 500, 300)
#well_result(12611029.85, 7994974.627, 12611029.85, 7994974.627, 90, 500, 300)
#well_result(12611029.85, 7994974.627, 12611029.85, 7994974.627, 135, 500, 300)
#well_result(12611029.85, 7994974.627, 12611029.85, 7994974.627, 180, 500, 300)
##well_result(12611029.85, 7994974.627, 12611029.85, 7994974.627, 225, 500, 300)
#well_result(12611029.85, 7994974.627, 12611029.85, 7994974.627, 270, 500, 300)
#well_result(12611029.85, 7994974.627, 12611029.85, 7994974.627, 315, 500, 300)
# map1 = third_point(12604448.33, 7993175.934, 12604448.33, 7993175.934, 0, 500)
# map1 = my_well(12604448.33, 7993175.934, 12604448.33, 7993175.934, 0, 500, map1.read_file(), 300)
# map1.display_info()
