path_infile = r'C:\1\1_Field\Multi_var_2\18_10_years_project_well\project_wells\WELLTRACK_2.txt'
path_outfile = r'C:\1\1_Field\Multi_var_2\18_10_years_project_well\project_wells\FRACFILE_new2.txt'

#path_infile = "C:\\1\\1_Field\\OPR\\WELLTRACK_2.txt"
#path_outfile = "C:\\1\\1_Field\\OPR\\FRACFILE_new2.txt"


def writeFractuleFile(MD, number_well, path_outfile):
    #list_of_Ach2 = ["3-6", "3-7", "3-8", "3-9"]
    #print(number_well)
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

        #if number_well in list_of_Ach2:
        #    out_file.write("\t\'2.txt\'\t/\n")
        #else:
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
        #print(lines[i])
        if len(lines[i]) > 0 and lines[i][0] == "WELLTRACK":
            number_well = lines[i][1]
            #print(number_well)
        elif len(lines[i]) == 4:
            MD.insert(0, float(lines[i][3]))
            #print(MD)
        elif (len(lines[i]) > 0 and lines[i][0] == "/"):
            #print(lines[i][0])
            writeFractuleFile(MD, number_well, path_outfile)
            MD.clear()

        i = i + 1

    in_file.close()
    out_file = open(path_outfile, 'a')
    out_file.write("/\n")

readInFile(path_infile, path_outfile)