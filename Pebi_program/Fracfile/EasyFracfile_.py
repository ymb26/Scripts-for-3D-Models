path_infile = r'C:\1\4_Scripts\Test_EasyFracfile\23_MVR_2_case\WELLTRACKS\WELLTRACK_longitudinal.txt'
path_outfile = r'C:\1\4_Scripts\Test_EasyFracfile\23_MVR_2_case\Fracfiles\Fracfile_300_75_standart_12_longitudinal.txt'

def writeFractuleFile(MD, number_well, path_outfile):
    out_file = open(path_outfile, 'a')
    i = 0
    while i < len(MD):
        if MD[i] == 0:
            out_file.write("\n")
            break
        out_file.write(str(number_well) + "_stage_" + str(i + 1) + '\t1\t' + "JUN\t2023\tMD\t" + str(round(MD[i], 1)) + '\t')
        if i == 0:
            out_file.write(str(round(MD[i], 1) - 0.5))
        else:
            out_file.write(str(round(MD[i], 1) + 0.5))

        out_file.write("\t\'%s.txt\'\t/\n" % number_well)
        i += 1


def readInFile(path_infile, path_outfile):
    in_file = open(path_infile, 'r')
    out_file = open(path_outfile, 'w')
    out_file.write("FRACFILE\n\n")
    out_file.close()

    lines = [line.split() for line in in_file]

    i = 0
    MD = list()
    #
    while (i < len(lines)):
        if len(lines[i]) > 0 and lines[i][0] == "WELLTRACK":
            number_well = lines[i][1]
        elif len(lines[i]) == 4:
            MD.insert(0, float(lines[i][3]))
        elif (len(lines[i]) > 0 and lines[i][0] == "/"):
            writeFractuleFile(MD, number_well, path_outfile)
            MD.clear()

        i = i + 1

    in_file.close()
    out_file = open(path_outfile, 'a')
    out_file.write("/\n")

readInFile(path_infile, path_outfile)