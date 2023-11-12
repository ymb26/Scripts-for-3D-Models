import numpy as np

def makeMatrix(perm_list, fracmult_list, data_path):
    for i in perm_list:
        for j in fracmult_list:
            with open(data_path + "\\3!!Orenburg_test_PERM2_FM15.data", 'r', errors='ignore') as f:
                old_data = f.read()
                #print(old_data)
            if j == 1.5:
                new_data2 = old_data.replace('FRACMULT.txt', 'FRACMULT_1_5.txt')
            else:
                new_data2 = old_data.replace('FRACMULT.txt', 'FRACMULT_' + str(round(j, 1)) + '.txt')

            new_datax = new_data2.replace('PERMX=PERMX*2', 'PERMX=PERMX*' + str(round(i, 1)))
            new_datay = new_datax.replace('PERMY=PERMY*2', 'PERMY=PERMY*' + str(round(i, 1)))
            new_dataz = new_datay.replace('PERMZ=PERMZ*2', 'PERMZ=PERMZ*' + str(round(i, 1)))

            if j == 1.5 and i == 1.5:
                name = data_path + "\\3_PERM_1_5" + "_FM_1_5" + ".data"
            elif j == 1.5:
                name = data_path + "\\3_PERM" + str(round(i, 1)) + "_FM_1_5" + ".data"
            elif i == 1.5:
                name = data_path + "\\3_PERM_1_5" + "_FM_" + str(round(j, 1)) + ".data"
            else:
                name = data_path + "\\3_PERM" + str(round(i, 1)) + "_FM_" + str(round(j, 1)) + ".data"
            with open(name, 'w') as f:
                f.write(new_dataz)

            new_data_without_frac = new_dataz.replace('FRAC_SIMP=0.1	--', '--FRAC_SIMP=0.1	--')
            name2 = name.replace(".data", "_v2.data")
            with open(name2, 'w') as f2:
                f2.write(new_data_without_frac)

            print(name)
            print(name2)


####################################################
data_path = r'\\10.10.1.79\pgsmb\12. Exchange\Yuri_Baronov\ORENBURG3'

#perm_list = [1.5, 2, 3, 3.5]
#fracmult_list = [1.5, 2, 3, 5]
#perm_list = [1]
#fracmult_list = [1]

makeMatrix([1.5, 2, 3, 3.5], [1.5, 2, 3, 5], data_path)
makeMatrix([1], [1], data_path)
####################################################