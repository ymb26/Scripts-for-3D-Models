import time
start_time = time.time()
amount_fipnums = 8
i_max = 123
j_max = 145
k_max = 175
path = "C:\\Users\\Y_Baronov\\Y\\1\\Новая папка\\TAS_EO1_PK1-8\\GRID\\ACTNUM1.GRDECL"
path_output = "C:\\Users\\Y_Baronov\\Y\\1\\Новая папка\\TAS_EO1_PK1-8\\AQUA\\PK1-8_aqua2.inc"
output_fipnum = "C:/Users/Y_Baronov/Y/1/Новая папка/TAS_EO1_PK1-8/AQUA/Aqua_fipnum_%i.inc"
def console_picture():
    print("*************************************************************************")
    print("*************************************************************************")
    print("**            ********       *********        **          **       *******                                      **")
    print("**           **          **      *********        **          **      **          **                                   **")
    print("**           **          **      **          **        **          **      **          **                                   **")
    print("**           **          **      **          **        **          **      **          **                                   **")
    print("**           *********      **          **        **          **      *********                                   **")
    print("**           *********      **          **        **          **      *********                                   **")
    print("**           **          **      *********        **          **      **          **                                   **")
    print("**           **          **      *********        *********      **          **                                   **")
    print("**           **          **                    ****       *******       **          **                                   **")
    print("*************************************************************************")
    print("*************************************************************************\n")
console_picture()
def make_array(i_max, j_max, k_max, path):
    Composition = i_max * j_max * k_max
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
    param = param1[len(param1) - Composition - 1:]
    array_3d = [[[0 for i in range(i_max)] for j in range(j_max)] for k in range(k_max)]
    for k in range(k_max):
        for j in range(j_max):
            for i in range(i_max):
                if param[index] == '/':
                    break
                array_3d[k][j][i] = param[index]
                index = index + 1
    return (array_3d)
time1 = time.time()
def aguancon_file(i_max, j_max, k_max, path, path_output):
    array_Atcn = make_array(i_max, j_max, k_max, path)
    print("Время создания 3-х мерного массива --- %s seconds ---" % (time.time() - start_time))
    output_test = open(path_output, "w")
    output_test.write("AQUANCON\n")
    for k in range(k_max):
        for j in range(j_max):
            i = 0
            while (i < i_max) and (array_Atcn[k][j][i] != '1'):
                i = i + 1
                if (i < i_max):
                    if 0 <= k < 28:
                        fipnum_number = 1
                    elif 28 < k < 54:
                        fipnum_number = 2
                    elif 54 < k < 75:
                        fipnum_number = 3
                    elif 75 < k < 97:
                        fipnum_number = 4
                    elif 97 < k < 114:
                        fipnum_number = 5
                    elif 114 < k < 131:
                        fipnum_number = 6
                    elif 131 < k < 159:
                        fipnum_number = 7
                    elif 159 < k < 175:
                        fipnum_number = 8
                    else:
                        fipnum_number = 0
                    str1 = " " + str(fipnum_number) + " " + str(i + 1) + " " + str(i + 1) + " " + str(j + 1) + " " + str(j + 1) + " " + str(k + 1) + " " + str(k + 1) + " I- 1* 1* NO /\n"
                    output_test.write(str1)

    for k in range(k_max):
        for j in range(j_max):
            i = i_max - 1
            while (0 < i) and (array_Atcn[k][j][i] != '1'):
                i = i - 1
                if (0 < i):
                    if 0 <= k < 28:
                        fipnum_number = 1
                    elif 28 < k < 54:
                        fipnum_number = 2
                    elif 54 < k < 75:
                        fipnum_number = 3
                    elif 75 < k < 97:
                        fipnum_number = 4
                    elif 97 < k < 114:
                        fipnum_number = 5
                    elif 114 < k < 131:
                        fipnum_number = 6
                    elif 131 < k < 159:
                        fipnum_number = 7
                    elif 159 < k < 175:
                        fipnum_number = 8
                    else:
                        fipnum_number = 0
                    str1 = " " + str(fipnum_number) + " " + str(i + 1) + " " + str(i + 1) + " " + str(j + 1) + " " + str(j + 1) + " " + str(k + 1) + " " + str(k + 1) + " I+ 1* 1* NO /\n"
                    output_test.write(str1)

    for k in range(k_max):
        for i in range(i_max):
            j = j_max - 1
            while (0 < j) and (array_Atcn[k][j][i] != '1'):
                j = j - 1
                if (0 < j):
                    if 0 <= k < 28:
                        fipnum_number = 1
                    elif 28 < k < 54:
                        fipnum_number = 2
                    elif 54 < k < 75:
                        fipnum_number = 3
                    elif 75 < k < 97:
                        fipnum_number = 4
                    elif 97 < k < 114:
                        fipnum_number = 5
                    elif 114 < k < 131:
                        fipnum_number = 6
                    elif 131 < k < 159:
                        fipnum_number = 7
                    elif 159 < k < 175:
                        fipnum_number = 8
                    else:
                        fipnum_number = 0
                    str1 = " " + str(fipnum_number) + " " + str(i + 1) + " " + str(i + 1) + " " + str(j + 1) + " " + str(j + 1) + " " + str(k + 1) + " " + str(k + 1) + " J+ 1* 1* NO /\n"
                    output_test.write(str1)

    for k in range(k_max):
        for i in range(i_max):
            j = 0
            while (j < j_max) and (array_Atcn[k][j][i] != '1'):
                j = j + 1
                if (j < j_max):
                    if 0 <= k < 28:
                        fipnum_number = 1
                    elif 28 < k < 54:
                        fipnum_number = 2
                    elif 54 < k < 75:
                        fipnum_number = 3
                    elif 75 < k < 97:
                        fipnum_number = 4
                    elif 97 < k < 114:
                        fipnum_number = 5
                    elif 114 < k < 131:
                        fipnum_number = 6
                    elif 131 < k < 159:
                        fipnum_number = 7
                    elif 159 < k < 175:
                        fipnum_number = 8
                    else:
                        fipnum_number = 0
                    str1 = " " + str(fipnum_number) + " " + str(i + 1) + " " + str(i + 1) + " " + str(j + 1) + " " + str(j + 1) + " " + str(k + 1) + " " + str(k + 1) + " J- 1* 1* NO /\n"
                    output_test.write(str1)

    output_test.write("/\n")
    output_test.close()
aguancon_file(i_max, j_max, k_max, path, path_output)
time2 = time.time()
print("Время создания файла аквифер для всех пластов --- %s seconds ---" % (time2 - time1))
def output_aqua_fipnum(path_output, output_fipnum):
    fn = open(path_output, "r")
    f = open(output_fipnum % x, 'w')
    f.write("AQUANCON\n")
    for i, line in enumerate(fn):
        if line[1] == '%a' % x:
            f.write(line)
    f.write("/\n")
    f.close()
for x in range(1, amount_fipnums + 1):
    output_aqua_fipnum(path_output, output_fipnum)
time3 = time.time()
print("Время создания файлов: аквиферы по пластам--- %s seconds ---" % (time3 - time2))
print("Время выполнения всех скриптов--- %s seconds ---" % (time.time() - start_time))