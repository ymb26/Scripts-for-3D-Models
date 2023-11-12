
import pandas as pd
'''
path = r'Y:\MVR_ORENBURG\2_iter\additional\5_portov\Hist_prognoz.txt'
df = pd.read_csv(path, delimiter='\t', header=0)
print(df[])
#df.loc[((df['RAD'] > 110))].to_csv(r'C:\1\1_Field\216\RECU_216_Kust_NewFrac_100bar!_cut.txt', sep='\t', index=False)
#print(df)
df_max = df.groupby('EFORM').max()
print(df_max)
#print(df_max.loc['21601', 'RAD'])
'''


path = r'C:\1\Cut_files\1.txt'
df = pd.read_csv(path, delimiter='\t', header=0)
df_max = df.groupby('EFORM')['WELL'].max()
for i in df_max:
    print(i)