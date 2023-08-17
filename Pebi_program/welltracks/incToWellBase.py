import pandas as pd
import os
path_in = r'\\10.10.2.235\пао газпромнефть\ХАНТОС\Приобское_ЗКАТ\2023\2_ГМ\2_Раб.материалы\NEW_GM_ot_15_05_2023\inkl'
welltrack_path = r'C:\1\1_Field\PRIOBKA\welltrack_nns.inc'
with open(welltrack_path, 'w') as f:
    print()

for root, dirs, files in os.walk(path_in):
    for file in files:
        if '.' not in file:
            name = file
            print(os.path.join(root, file))
            #path = r'\\10.10.2.235\пао газпромнефть\ХАНТОС\Приобское_ЗКАТ\2023\2_ГМ\2_Раб.материалы\NEW_GM_ot_15_05_2023\inkl\%s' %name
            df = pd.read_table(os.path.join(root, file),
                               names=['MD', 'X', 'Y', 'Z', 'TVD', 'DX', 'DY', 'AZIM_TN', 'INCL', 'DLS', 'AZIM_GN'],
                               skiprows=17, sep=' ')
            df.loc[df['Z'] != 0, 'Z'] *= -1
            with open(welltrack_path, 'a') as f:
                f.write("WELLTRACK %s\n" %name)
            df.to_csv(welltrack_path, mode='a', columns=['X', 'Y', 'Z', 'MD'], sep=' ', header=False, index=False)
            with open(welltrack_path, 'a') as f:
                f.write("/\n\n")
        if '.dev' in file:
            name = file[:-4]
            print(os.path.join(root, file))
            #path = r'\\10.10.2.235\пао газпромнефть\ХАНТОС\Приобское_ЗКАТ\2023\2_ГМ\2_Раб.материалы\NEW_GM_ot_15_05_2023\inkl\%s' %name
            df = pd.read_table(os.path.join(root, file),
                               names=['MD', 'X', 'Y', 'Z', 'TVD', 'DX', 'DY', 'AZIM_TN', 'INCL', 'DLS', 'AZIM_GN'],
                               skiprows=17, sep=' ')
            df.loc[df['Z'] != 0.0, 'Z'] *= -1
            with open(welltrack_path, 'a') as f:
                f.write("WELLTRACK %s\n" %name)
            df.to_csv(welltrack_path, mode='a', columns=['X', 'Y', 'Z', 'MD'], sep=' ', header=False, index=False)
            with open(welltrack_path, 'a') as f:
                f.write("/\n\n")

#path = r'\\10.10.2.235\пао газпромнефть\ХАНТОС\Приобское_ЗКАТ\2023\2_ГМ\2_Раб.материалы\NEW_GM_ot_15_05_2023\inkl\216\21615'
#df = pd.read_table(path, names=['MD', 'X', 'Y', 'Z', 'TVD', 'DX','DY', 'AZIM_TN', 'INCL', 'DLS', 'AZIM_GN'],skiprows=17, sep=' ')
#df.loc[df['Z'] != 0, 'Z'] *=  -1
#with open(welltrack_path, 'a') as f:
#    f.write("WELLTRACK \n")
#df.to_csv(welltrack_path, mode='a', columns=['X', 'Y', 'Z', 'MD'], sep=' ', header=False, index=False)
#with open(welltrack_path, 'a') as f:
#    f.write("/\n")
