import os
#path_infile = "C:\\1\\1_Field\\OPR\\WELLTRACK_2.txt"
#path_outfile = "C:\\1\\1_Field\\OPR\\FRACFILE_new2.txt"

def makeDataFiles(path_in, path_out, type_design, value, folder_of_length, number_well, name_of_wracfile_path, amount_of_stages, count):

    file_in = open(path_in, "r")
    file_out = open(path_out, "w")

    list_of_file = open(r'C:\1\1_Field\Multi_var_2\23_MVR_additional_cases\list_of_data.txt', 'a')  ####
    list_of_file.write(path_out + '\n')
    list_of_file.close()

    data = file_in.read()
    data = data.replace('\'FRACFILE_666.txt\'\n/\nINCLUDE\n\'WELLTRACK_666.txt\'', '\'%s\'\n/\nINCLUDE\n\'WELLTRACKS/WELLTRACK_%s_%s.txt\'' % (name_of_wracfile_path, folder_of_length, amount_of_stages))
    #print(count, "done")

    file_out.write(data)

    file_in.close()
    file_out.close()

def writeFractuleFile(MD, number_well, path_outfile, type_design, value, folder_of_length, amount_of_stages):
    out_file = open(path_outfile, 'a')
    i = 0
    while i < len(MD):
        if MD[i] == 0:
            out_file.write("\n")
            break
        out_file.write(str(number_well) + "_stage_" + str(i + 1) + '\t1\t' + "JUL\t2023\tMD\t" + str(round(MD[i], 1)) + '\t')
        if i == 0:
            out_file.write(str(round(MD[i], 1) - 0.5))
        else:
            out_file.write(str(round(MD[i], 1) + 0.5))

        #twelve_stages = [0, 1, 2, 10]
        #fifteen_stages = [0, 1, 2, 3, 7, 12]
        #if folder_of_length == 700 and int(number_well) == 1:
        #    if int(amount_of_stages) == 12 and i in twelve_stages:
        #        out_file.write("\t\'Fracfiles/%s/%s%s%s_Ach5.txt\'\t/\n" % (folder_of_length, number_well, type_design, value))
        #    elif int(amount_of_stages) == 15 and i in fifteen_stages:
        #        out_file.write("\t\'Fracfiles/%s/%s%s%s_Ach5.txt\'\t/\n" % (folder_of_length, number_well, type_design, value))
        #    else:
        #        out_file.write("\t\'Fracfiles/%s/%s%s%s.txt\'\t/\n" % (folder_of_length, number_well, type_design, value))
        #else:
        #    out_file.write("\t\'Fracfiles/%s/%s%s%s.txt\'\t/\n" % (folder_of_length, number_well, type_design, value))
        out_file.write("\t\'Fracfiles/%s/%s%s%s.txt\'\t/\n" % (folder_of_length, number_well, type_design, value))
        i += 1


def readInFile(path_infile, path_outfile, type_design, value, folder_of_length, amount_of_stages, name_of_wracfile_path, count):
    #print(path_outfile)
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
            writeFractuleFile(MD, number_well, path_outfile, type_design, value, folder_of_length, amount_of_stages)
            MD.clear()
        i = i + 1

    in_file.close()
    out_file = open(path_outfile, 'a')
    out_file.write("/\n")

    path_data_file = r'C:\1\1_Field\Multi_var_2\24_MVR_600_m\L_base_for_mvr.data'   ####
    path_out_data_file = r'C:\1\1_Field\Multi_var_2\24_MVR_600_m'                                    ####
    makeDataFiles(path_data_file, path_out_data_file + '\L_' + str(folder_of_length) + "_" + str(value) + str(type_design) + str(amount_of_stages) + '.data', type_design, value, folder_of_length, number_well, name_of_wracfile_path, amount_of_stages, count)

def findAllFiles():
    #path_in = r'C:\1\2_Work_files\SPD\MVR\ForGDM'
    #path_out = r'C:\1\2_Work_files\SPD\MVR\Fracfiles\Test_multi_out'
    path_in = r'C:\1\1_Field\Multi_var_2\24_MVR_600_m\WELLTRACKS\600_M_welltrack'            ####
    path_out = r'C:\1\1_Field\Multi_var_2\24_MVR_600_m\Fracfiles'            ####

    #list_of_file = open(r'C:\1\1_Field\Multi_var_2\23_MVR_additional_cases\list_of_data.txt', 'w')    ####
    #list_of_file.close()

    #variant_mass_of_prop = {300: [75, 100, 125, 150], 500: [75, 100, 125, 150, 175, 200], 700: [150, 175, 200, 225, 250]}
    #variant_type_of_design = {500: ["_hybrid_", "_hybridPAA_", "_standart_"], 300:["_standart_"], 700:["_hybrid_", "_hybridPAA_"]}

    variant_mass_of_prop = {300: [], 500: [], 700: [], 600: [75, 100, 125, 150, 175, 200, 225, 250] }  ###### change
    variant_type_of_design = {500: [], 300:[], 700:[], 600:["_hybrid_", "_hybridPAA_"]}   ###### change
    variant_stages = [12]   ###### change

    count = 1
    for root, dirs, files in os.walk(path_in):
        for file in files:
            if file.endswith(".txt"):
                name = str(os.path.join(root, file))[str(os.path.join(root, file)).rfind('\\') + 1:-4]
                folder_of_length = int(name[-6:-3])
                print(name, folder_of_length)
                #amount_of_stages = int(name[-2:])
                for amount_of_stages in variant_stages:
                    #print(amount_of_stages)
                    for value in variant_mass_of_prop[folder_of_length]:
                        #print(value)
                        for type_design in variant_type_of_design[folder_of_length]:
                            name_of_wracfile_path = "Fracfiles/Fracfile_" + str(folder_of_length) + "_" + str(value) + str(type_design) + str(amount_of_stages) + '.txt'
                            readInFile(os.path.join(root, file), path_out + "\Fracfile_" + str(folder_of_length) + "_" + str(value) + str(type_design) + str(amount_of_stages) + '.txt', type_design, value, folder_of_length, amount_of_stages, name_of_wracfile_path, count)
                            count += 1

if __name__ == "__main__":
    findAllFiles()
