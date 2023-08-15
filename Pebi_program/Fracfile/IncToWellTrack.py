import pandas as pd
import openpyxl
import numpy as np
import os


def makeWellTrack(path_in, path_out):
    #path_in = r'C:\1\2_Work_files\SPD\MVR\test.xlsx'
    #path_out = r'C:\1\2_Work_files\SPD\MVR\ForGDM\WellTrac_300_m_12_stad.txt'

    file_out = open(path_out, 'w')
    df = pd.read_excel(path_in, header=None)

    for row in df.itertuples(index=False):
        if 'MD' in row:
            df.columns = list(row)
            df.rename(columns={df.columns[0]: 'Stade'}, inplace=True)
            break
    for idx, row in df.iterrows():
        if row['MD'] == 0:
            file_out.write("WELLTRACK %s\n" % df.iloc[idx - 1]['Stade'])
        elif row['MD'] == "MD":
            continue
        #elif row['Stade'] == 1:
        #    file_out.write("%f\t%f\n/\n\n" % (row['X'], row['Y']))       ##
        elif np.isnan(row['Stade']):
            continue
        #if row['Stade'] == 1:
        #    file_out.write("%f\t%f\t%f\t%f\n" % (row['X'], row['Y'], -1 * row['Z'], row['MD'] - 0.5))            ## write coord
        #    file_out.write("/\n\n")       ##
        #elif df.iloc[idx - 1]['MD'] == 0:
        #    file_out.write("%f\t%f\t%f\t%f\n" % (row['X'], row['Y'], -1 * row['Z'], row['MD'] + 0.5))            ## write coord
        #else:
        #    file_out.write("%f\t%f\t%f\t%f\n" % (row['X'], row['Y'], -1 * row['Z'], row['MD']))
        if row['Stade'] == 1:
            file_out.write("%f\t%f\t%f\t%f\n" % (row['X'], row['Y'], -1 * row['Z'], row['MD']))
            file_out.write("/\n\n")
        else:
            file_out.write("%f\t%f\t%f\t%f\n" % (row['X'], row['Y'], -1 * row['Z'], row['MD']))
    file_out.close()
    #############################################################


def findAllFiles():
    path_in = r'C:\1\1_Field\Multi_var_2\26_MVR_300_m_kust\WELLTRACKS\300_M_welltrack_kust'
    path_out = r'C:\1\1_Field\Multi_var_2\26_MVR_300_m_kust\WELLTRACKS\300_M_welltrack_kust'
    count = 1
    for root, dirs, files in os.walk(path_in):
        for file in files:
            if file.endswith(".xlsx"):
                print(count)
                count += 1
                name = str(os.path.join(root, file))[str(os.path.join(root, file)).rfind('\\') + 1:-5]
                print(path_out + '\WELLTRACK_' + name)
                makeWellTrack(os.path.join(root, file), path_out + '\WELLTRACK_' + name + '.txt')



if __name__ == "__main__":
    findAllFiles()
