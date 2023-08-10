import pandas as pd
from datetime import datetime
from datetime import timedelta, date

'''
notOlga = ["21501", "21601", "21602", "21603", "21604", "21605", "21606", "21607", "21608", "21609", "21610", "21611", "21612", "22102", "22103", "22104", "22106", "22107", "22112", "22113", "22114", "22115", "22117", "22118", "22121", "22138", "22139", "22141", "22143", "22148", "22149", "22150", "22151", "22152", "22153", "22154", "22156", "22158", "22159", "22160", "42929", "42930", "42931", "42932", "42933", "42934", "42935", "42936", "42958", "42959", "42960", "42962", "42963", "42964", "42965", "42966", "42967", "42968", "43723", "43724", "43785", "215WZ", "perebur-22155", "Poz-1", "Poz-3", "Poz-4", "Poz-5", "Poz-6", "Poz-7", "Poz-8", "Poz-9"]
#notOlga = ["22102", "22103", "22104", "22106", "22117", "22115", "22118", "22114", "22113", "21602", "21603", "21604", "21607", "21605", "21606", "21609", "21611", "21608", "21610", "21612", "21614", "21615", "21616", "21617", "21618", "21619", "21620", "220ВЗ", "21502", "21503", "21504", "21505", "21509", "21508", "21507", "21506", "42929", "42930", "42931", "43723", "43724", "42932", "42937", "42933", "42934", "42935", "42958", "42936", "42960", "42959", "42965", "21501", "42968", "42967", "42966", "42964", "42963", "43785", "42962", "22112", "22121", "22141", "22138", "22139", "22143"]
path = r'C:\1\1_Field\PRIOBKA\Priobskoe_zapusk_221\20230310_RECU_FORECAST_NOPPD_NEW110.INC'
df = pd.read_csv(path, delimiter='\t', header=0)
#print(df)
df2 = df[df['WELL'].isin(notOlga)]
print(df2)
df2.to_csv(r'C:\1\1_Field\PRIOBKA\100\no_olga.INC', sep='\t', index=False)
'''

'''
path = r'C:\1\1_Field\PRIOBKA\100\no_olga_and_olga.INC'
df = pd.read_csv(path, delimiter='\t', header=0)

df['new_date'] = pd.to_datetime(df['\'DD.MM.YYYY\''], format='%d.%m.%Y')
df = df.sort_values(by='new_date', ascending=True)
df.to_csv(r'C:\1\1_Field\PRIOBKA\100\new_recu_sort.INC', sep='\t', columns=['WELL', '\'DD.MM.YYYY\'', 'MDL', 'MDU', 'RAD', 'SKIN'], index=False)
print(df)
'''

path = r'C:\1\4_Scripts\20230803_RECU_FORECAST_NOPPD_NEW50_new_data_sort_Y.INC'
df = pd.read_csv(path, delimiter='\t', header=0)
df['new_date'] = pd.to_datetime(df['\'DD.MM.YYYY\''], format='%d.%m.%Y')
df = df.sort_values(by='new_date', ascending=True)
df.to_csv(r'C:\1\4_Scripts\20230803_RECU_FORECAST_NOPPD_NEW50_new_data_sort_Y2.INC', sep='\t', columns=['WELL', '\'DD.MM.YYYY\'', 'MDL', 'MDU', 'RAD', 'SKIN'], index=False)
##################df['new_date'] = df['new_date'] - timedelta(days=1)
print(df)

#massive = {"22102": "13.02.2022", "22105": "28.03.2022", "22137": "11.09.2022", "22110": "26.10.2022", "22127": "08.12.2022", "22108": "15.02.2023", "22115": "22.10.2023", "22114": "13.01.2024", "22113": "23.02.2024", "22120": "27.06.2024", "22122": "20.09.2024", "22126": "23.02.2025", "22121": "29.07.2025", "22138": "10.11.2025", "22143": "22.02.2026", "22140": "15.04.2026", "22133": "06.06.2026", "22132": "09.11.2026", "22144": "31.12.2026", "22131": "17.09.2027", "22130": "08.11.2027"}
#dict ={}
#for keys in massive:
 #   print(keys)
