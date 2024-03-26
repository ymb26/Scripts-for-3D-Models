import os


frac_path = r'Y:\MVR_ORENBURG\7_iter_check_frac\All_frac_from_Artem\Check_result\FRACFILES'
data_path_base = r'Y:\MVR_ORENBURG\7_iter_check_frac\All_frac_from_Artem\Check_result\3_sector'
fracfile_path = r'Y:\MVR_ORENBURG\7_iter_check_frac\All_frac_from_Artem\Check_result\FRACFILES\Fracfile_7'

count = 0
for root, dirs, files in os.walk(frac_path):
    count += 1
    print(count, root)
    '''
    with open(fracfile_path + ".txt", 'r', errors='ignore') as file:
        old_data = file.read()
    new_data = old_data.replace('xxx.txt', "FRACFILES/%s/DESIGN_stage_01_01.txt" % root[root.rfind('\\')+1:])
    with open(fracfile_path + '_' + root[root.rfind('\\')+1:] + ".txt", 'w') as file2:
        file2.write(new_data)
    '''

    with open(data_path_base + ".data", 'r', errors='ignore') as file:
        old_data = file.read()
    new_data = old_data.replace('FRACFILES\Fracfile_7.txt',
                                'FRACFILES\Fracfile_7_%s.txt' % root[root.rfind('\\') + 1:])
    if 'GELACID' in root[root.rfind('\\') + 1:]:
        new_data2 = new_data.replace('EXP 0.5 0.005', 'EXP 0.15 0.004')  ##015 0005
        name = data_path_base + "_frac_k015_a0004_" + root[root.rfind('\\') + 1:]
    # elif 'PAA' in root[root.rfind('\\')+1:]:
    else:
        new_data2 = new_data.replace('EXP 0.5 0.005', 'EXP 0.12 0.005')  ##015 0005
        name = data_path_base + "_frac_k012_a0005_" + root[root.rfind('\\') + 1:]
    count += 1
    print(count, name + ".data")
    with open(name + ".data", 'w') as file2:
        file2.write(new_data2)

