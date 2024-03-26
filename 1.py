import filecmp

path = r'Y:\MVR_ORENBURG\5_iter\6_optimal\FRACFILES'

filecmp.cmp(path + "\ACIDPROP_Prop_10_Acid_50_rate_4\DESIGN_stage_01_01.txt", path + "\ACIDPROP_Prop_10_Acid_50_rate_4\DESIGN_stage_01_01.txt")
filecmp.cmp(path + "\ACIDPROP_Prop_10_Acid_50_rate_4\DESIGN_stage_01_01.txt", path + "\ACIDPROP_Prop_10_Acid_50_rate_4\DESIGN_stage_01_01.txt", shallow=False)