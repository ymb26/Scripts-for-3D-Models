import pandas as pd
from datetime import datetime
from datetime import timedelta, date

path = r'C:\Users\baronov.ym\Desktop\1.txt'
well_list = ["43724", "42934G", "22102G", "22105G", "42935G", "22137", "22110G", "22127", "42964", "22108G", "22101", "22106", "22111", "42929", "42962", "42963", "42966", "42967", "42968", "22103G", "22104G", "22109G", "22155ST2", "42931G", "42936G", "42958G"]
df = pd.read_csv(path, delimiter='\t', header=0)

print(df)
print(df.loc[df['EFORM']. isin(well_list)])

df.loc[df['EFORM']. isin(well_list)].to_csv(r'C:\Users\baronov.ym\Desktop\2.txt', sep='\t', index=False)

