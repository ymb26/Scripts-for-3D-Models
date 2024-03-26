import os


frac_folder = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

frac_path = r'Y:\MVR_ORENBURG\7_iter_check_frac\All_frac_from_Artem\Check_result\FRACFILES'
data_path_base = r'Y:\MVR_ORENBURG\7_iter_check_frac\All_frac_from_Artem\Check_result\3_sector'
fracfile_path = r'Y:\MVR_ORENBURG\7_iter_check_frac\All_frac_from_Artem\Check_result\FRACFILES\Fracfile_7'

'''

#for root, dirs, files in os.walk(frac_path):
    #print(root)
count = 0
for frac in frac_folder:
    #print(frac_path + '\\' + frac)
    for root, dirs, files in os.walk(frac_path + '\\' + frac):
        #'''#
        print(root[root.rfind('\\')+1:])
        #with open(fracfile_path + ".txt", 'r', errors='ignore') as file:
        #    old_data = file.read()
        #new_data = old_data.replace('xxx.txt', "FRACFILES/%s/%s/DESIGN_stage_01_01.txt" % (frac, root[root.rfind('\\')+1:]))
        #with open(fracfile_path + "_" + frac + '_' + root[root.rfind('\\')+1:] + ".txt", 'w') as file2:
        #    file2.write(new_data)
        #
        print('----------------------------------------------------------------')
        #'''
        with open(data_path_base + ".data", 'r', errors='ignore') as file:
            old_data = file.read()
        new_data = old_data.replace('FRACFILES\Fracfile_7.txt', 'FRACFILES\Fracfile_7_%s_%s.txt' % (frac, root[root.rfind('\\')+1:]))
        if 'GELACID' in root[root.rfind('\\')+1:]:
            new_data2 = new_data.replace('EXP 0.5 0.005', 'EXP 0.15 0.004')   ##015 0005
            name = data_path_base + "_frac_k015_a0004_" + frac + '_' + root[root.rfind('\\')+1:]
        #elif 'PAA' in root[root.rfind('\\')+1:]:
        else:
            new_data2 = new_data.replace('EXP 0.5 0.005', 'EXP 0.12 0.005')  ##015 0005
            name = data_path_base + "_frac_k012_a0005_" + frac + '_' + root[root.rfind('\\') + 1:]
        count += 1
        print(count, name + ".data")
        with open(name + ".data", 'w') as file2:
            file2.write(new_data2)
        #'''
'''
