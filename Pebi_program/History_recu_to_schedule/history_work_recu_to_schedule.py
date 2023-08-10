import pandas as pd
from datetime import datetime


def fRoanding(number):
    return "{:.2f}".format(number)

in_path = r'C:\1\1_Field\PRIOBKA\Priobskoe_zapusk_221\20230803_RECU_FORECAST_NOPPD_NEW50_new_data_sort_Y.inc'
out_path = r'C:\1\1_Field\PRIOBKA\Priobskoe_zapusk_221\20230803_RECU_FORECAST_NOPPD_NEW50_new_data_sort_Y_recu_to_schedule.inc'

df = pd.read_csv(in_path, delimiter='\t', names=['WELL', 'DD.MM.YYYY', 'QOIL', 'QWAT', 'BHP', 'WEFA', 'QWIN', 'QGAS'])
df['DD.MM.YYYY'] = pd.to_datetime(df['DD.MM.YYYY'], dayfirst=True).dt.date
df2 = df.sort_values(by='DD.MM.YYYY', ascending=True)
df2['flag'] = df2['DD.MM.YYYY'].duplicated()
for row in df2.itertuples():
    print(row)
file_out = open(out_path, 'w')

for index, row in df2.iterrows():
    if not row['flag']:
        file_out.write("DATES\n" + str(row['DD.MM.YYYY'].day) + ' ' + str(row['DD.MM.YYYY'].strftime("%B").upper()[:3])
                       + ' ' + str(row['DD.MM.YYYY'].year) + "\t/\n/\n")
    file_out.write("WCONHIST\n")
    file_out.write("\'" + row['WELL'] + "\'" + '\t' + "\'OPEN\'\t\'LRAT\'\t" + str(fRoanding(row['QOIL'])) + '\t' +
                   str(fRoanding(row['QWAT'])) + '\t' + str(fRoanding(row['QGAS'])) + "\t3*\t" +
                   str(fRoanding(row['BHP'])) + "\t/\n/\n")
    file_out.write("WEFAC\n" + "\'" + str(row['WELL']) + "\'\t" + str(row['WEFA']) + "\t/\n/\n")
