import pandas as pd

path = r'C:\1\1_Field\216\RECU_216_Kust_NewFrac_50bar!.txt'
df = pd.read_csv(path, delimiter='\t', header=0)
#df.loc[((df['RAD'] > 110))].to_csv(r'C:\1\1_Field\216\RECU_216_Kust_NewFrac_100bar!_cut.txt', sep='\t', index=False)
#print(df)
df_max = df.groupby('EFORM').max()
print(df_max)
#print(df_max.loc['21601', 'RAD'])