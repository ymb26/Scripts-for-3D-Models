import os
import pandas as pd


input_path = r'C:\1\1_Field\South_Sunduk\WELLTRACKS\res_adapt!!!!'
output_path = r'C:\1\1_Field\South_Sunduk\WELLTRACKS\W'

for root, dirs, files in os.walk(input_path):
    for file in files:
        if '.xlsx' not in file:
            if '11-BGS' not in file:
                skiprow = 18
            else:
                skiprow = 16
            name_file = input_path + '\\' + file
            out_name_file = output_path + '\\WELLTRACK_' + file[file.rfind("!") + 1:] + '.txt'
            #print(out_name_file)
            with open(out_name_file, 'w') as file_writer:
                file_writer.write('WELLTRACK %s\n' % file[file.rfind("!") + 1:])
            df = pd.read_csv(name_file, skiprows=skiprow, sep=' ', names=['emp', 'MD', 'X', 'Y', 'Z', 'TVD', 'DX', 'DY', 'AZIM', 'INCL', 'DLS'])
            df.to_csv(out_name_file, columns=['X', 'Y', 'TVD', 'MD'], index=False, sep='\t', header=False, mode='a')
            with open(out_name_file, 'a') as file_writer:
                file_writer.write('\n/\n\n')
            print(file[file.rfind("!") + 1:])


