
stage = [5, 7, 9]
degr = ["degr1", "degr2"]
sector = [1, 2, 3, 4]
#frac = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
frac = [1, 2, 3, 4, 5, 6]
frac_name = ["6368P1c24", "1534P4c4", "1313P2c4rp03", "6368P2c1"]
frac_name2 = ["Acid_50m3_4", "Acid_50m3_6", "Acid_50m3_8", "Acid_100m3_4", "Acid_100m3_6", "Acid_100m3_8", "Acid_150m3_4", "Acid_150m3_6", "Acid_150m3_8", "GelAcid_50m3_70m3_10tone_4", "GelAcid_50m3_70m3_10tone_6", "GelAcid_50m3_70m3_10tone_8"]
frac_name3 = ["Acid_100m3_4", "Acid_100m3_6", "Acid_100m3_8", "GelAcid_50m3_70m3_10tone_4", "GelAcid_50m3_70m3_10tone_6", "GelAcid_50m3_70m3_10tone_8"]
#all_frac = ["6368P1c24", "1534P4c4", "1313P2c4rp03", "6368P2c1", "Acid_100m3_4", "Acid_100m3_6", "Acid_100m3_8", "GelAcid_50m3_70m3_10tone_4", "GelAcid_50m3_70m3_10tone_6", "GelAcid_50m3_70m3_10tone_8"]
#all_frac = ["GelAcid_Prop_10_Acid_50_gelacid_75_rate_4", "GelAcid_Prop_10_Acid_50_gelacid_75_rate_6", "GelAcid_Prop_10_Acid_50_gelacid_75_rate_8"]
#all_frac = ["AcidProp_Prop_10_Acid_50_gelacid_0_rate_4", "AcidProp_Prop_10_Acid_50_gelacid_0_rate_6", "AcidProp_Prop_10_Acid_50_gelacid_0_rate_8", "AcidProp_Prop_10_Acid_100_gelacid_0_rate_4", "AcidProp_Prop_10_Acid_150_gelacid_0_rate_4", "GelAcid_Prop_10_Acid_50_gelacid_75_rate_4", "GelAcid_Prop_10_Acid_50_gelacid_75_rate_6", "GelAcid_Prop_10_Acid_50_gelacid_75_rate_8", "6368_p2_c2-4_rp03_az", "1313_p2_c5_rp_06_az"]
#all_frac = ["6368_p1_c3-5_leaktweak_az", "6368_p1_c3-5_leaktweak1_6_az", "6368_p2_c3-5_rp06_az", "6368_p2_c3-5_rp07_az"]


#all_frac = ["1313_p2_c6_rp_06_az"]
#all_frac = ["1534_p4_c6_az"]
all_frac = ["6368_p1_c3-6_rp1_az", "6368_p2_c3-6_rp1_az"]

count = 0

'''
data_path = r'Y:\MVR_ORENBURG\2_iter\new_pressure\9_portov\FRACFILES\Fracfile_9'
for a in all_frac:
    with open(data_path + ".txt", 'r', errors='ignore') as file:
        old_data = file.read()

    new_data = old_data.replace('xxx.txt', "FRACFILES/%s/DESIGN_stage_01_01.txt" % a)
    with open(data_path + "_" + a + ".txt", 'w') as file2:
        file2.write(new_data)
'''
#'''
data_path = r'Y:\MVR_ORENBURG\2_iter\new_pressure\5_portov\3_sector'
for f in all_frac:
    with open(data_path + ".data", 'r', errors='ignore') as file:
        old_data = file.read()
    new_data = old_data.replace('FRACFILES\Fracfile_5.txt', 'FRACFILES\Fracfile_5_%s.txt' % f)
    new_datad = new_data.replace('EXP 0.5 0.005', 'EXP 0.5 0.01')
    new_datax = new_datad.replace('PERMX=PERMX*1		--', 'PERMX=PERMX*1.3		--')
    new_datay = new_datax.replace('PERMY=PERMY*1		--', 'PERMY=PERMY*1.3		--')
    new_dataz = new_datay.replace('PERMZ=PERMZ*1		--', 'PERMZ=PERMZ*1.3		--')
    ########---первый файл
    name = data_path + "_frac_k05_a001_" + f
    print(name + ".data")
    with open(name + ".data", 'w') as file2:
        file2.write(new_dataz)

    ########---копия с другой деградацией
    #name2 = data_path + "_frac_k05_a001_" + f
    #print(name2 + ".data")
    #with open(name2 + ".data", 'w') as file3:
    #    new_data2 = new_data.replace('EXP 0.5 0.005', 'EXP 0.5 0.01')
    #    file3.write(new_data2)

#'''