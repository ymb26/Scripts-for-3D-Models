import os


path_in = r'C:\1\1_Field\Multi_var_2\24_MVR_600_m\Fracfiles'
path_out = r'C:\1\1_Field\Multi_var_2\24_MVR_600_m\Fracfiles\new'

count = 1
for root, dirs, files in os.walk(path_in):
    for file in files:
        if file.endswith(".txt") and "Fracfile" in file and not "new" in root:
            print(count, file)
            with open(os.path.join(root, file), 'r') as file_in:
                file_out = open(os.path.join(path_out, file), 'w')
                for lines in file_in:
                    if "stage_1\t" in lines:
                        buff = [line for line in lines.split()]
                        buff_str = buff[5]
                        buff[5] = buff[6]
                        buff[6] = buff_str
                        file_out.write('\t'.join(buff))
                        file_out.write('\n')
                    else:
                        file_out.writelines(lines)

                count += 1
