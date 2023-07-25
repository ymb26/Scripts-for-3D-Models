import struct
import codecs

import np as np
# from pylab import plt
import numpy as np
# import matplotlib.colors as colors
import pandas as pd
import openpyxl
import io
from datetime import datetime
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta


'''
filename = r'C:\\1\\1_Field\\Р10-90_Oil_case\\Р75\\Data_P75_gmm50_0005\\Data_P75_gmm50.UNSMRY

with open(filename, 'rb') as file:
        for line in file:
            print(line)
            break

'''


# tested on python 2.7.10, matplotlib 1.4.3, numpy 1.10.1, pandas 0.17.0
# and python 3.5.0, matplotlib 1.4.3, numpy 1.10.1, pandas 0.17.0

def read_bin(filename):
    from struct import unpack
    from numpy import float32, uint32, uint8, dtype, float64, array, where
    bsdict, data = {b'REAL': (4, 'f', float32), b'INTE': (4, 'I', uint32), b'DOUB': (8, 'd', float64),
                    b'LOGI': (4, 'I', uint32), b'CHAR': (8, 's', dtype('a8'))}, {}
    with open(filename, 'rb+') as f:
        fr = f.read
        while 1:
            head = fr(20)
            if len(head) == 0:
                break;
            else:
                _, name, datalen, type = unpack('>L8sL4s', head)  # size = calcsize('>L8cL4c')
                name = name.strip()
                if datalen == 0:
                    break;
                else:
                    buf = unpack('>L', fr(8)[4:])[0]
                    bsize, fmt, npfmt = bsdict[type]
                    tchar = (1 if type != b'CHAR' else 0)
                    if buf == (bsize * datalen):
                        str1 = ('>%d%s' % (datalen, fmt) if tchar else ('>' + '8s' * datalen))
                        rd1 = fr(bsize * datalen)
                        m = unpack(str1, rd1)
                    else:
                        m = []
                        while len(m) < datalen:
                            m += unpack(('>%d%s' % (buf / bsize, fmt) if tchar else ('>' + '8s' * int(buf / bsize))),
                                        fr(buf))
                            buf = (unpack('>L', fr(8)[4:])[0] if len(m) < datalen else buf)
                    fr(4)
                    m = array(m, dtype=npfmt);
                    if name not in data:
                        data[name] = [m];
                    else:
                        data[name] += [m];
    return data


def get_tab_from_bin(casename):
    from numpy import array, compress, where
    from datetime import date
    from pandas import DataFrame, to_datetime
    def list_strip(lst):
        return list(map(lambda x: x.strip(), spec[lst][0]))

    spec = read_bin(casename + '.SMSPEC')  # Summary specification file
    kw, kn, un = list(map(list_strip, (b'KEYWORDS', b'WGNAMES', b'UNITS')))
    wells_list = list(set(kn) - set((':+:+:+:+',)))
    cols = [kw, kn, spec[b'NUMS'][0], un]  # 'NUMS' = CELL | REGION NUMBER
    unsmry = read_bin(casename + '.UNSMRY')  # Unified summary file
    df = DataFrame(array(unsmry[b'PARAMS']), columns=cols)
    del unsmry
    df['DAYS'] = df[b'TIME'].diff()
    # df.to_csv("C:\\1\\test.xls", sep='\t')
    # print(df)
    df = df.T.drop_duplicates().T  # WBHP duplicated in output
    return df, wells_list



# casename = r'C:\1\1_Field\Р10-90_Oil_case\Р75\Data_P75_gmm50_0005\Data_P75_gmm50'

# casename = r'C:\1\1_Field\Multi_var_2\23_MVR\L_300_75_standart_15_0000\L_300_75_standart_15'
casename = r'/Users/yurabaronov/Desktop/PHYSGEO/test_model/L_300_75_standart_15_0000/L_300_75_standart_15'
rdata_path = r'/Users/yurabaronov/Desktop/PHYSGEO/test_model/L_300_75_standart_15_0000/L_300_75_standart_15.rdata'

df, wells_list = get_tab_from_bin(casename)
wells_array = [b'1', b'2', b'3']  ##well list
wells_array_str = list()  ##well list - byte to str
for well in wells_array:
    wells_array_str.append(well.decode('utf-8'))
list_of_params = [b'WOPT', b'WWPT', b'WGPT', b'WIT']
arrays = [[], []]
useless_wells_byte = list(set(wells_list) - set(wells_array))
useless_wells_str = list()
for well in useless_wells_byte:
    useless_wells_str.append(well.decode('utf-8'))
list_of_params = [x for x in list_of_params if x in df]
df2 = df[list_of_params]
df2 = df2.rename(columns={b'WOPT': 'WOPT', b'WWPT': 'WWPT', b'WGPT': 'WGPT'})
df2 = df2.rename(columns={b'SM3': str('SM3')})
for well, well1 in zip(wells_array, wells_array_str):
    df2 = df2.rename(columns={well: well1})
for well, well1 in zip(useless_wells_byte, useless_wells_str):
    df2 = df2.rename(columns={well: well1})
for well in useless_wells_str:
    try:
        df2 = df2.drop(columns=well, level=1)
    except:
        continue
df2['Timesteps'] = df['DAYS']
df2['Times'] = df[b'TIME']
file = open(rdata_path, 'r').readlines()
for i in range(len(file)):
    if "START" in file[i]:
        start_date_str = file[i + 1][:file[i+1].find("/")].strip()
        break
start_date = datetime.strptime(start_date_str, "%d %b %Y")
time_array = [start_date + timedelta(days=step) for step in df2['Times']]


df2['Date'] = np.array(time_array)
##print(start_date + relativedelta(years=10))       #### plus years
work_wells = list()
sum_of_water = list()
sum_of_oil = list()
sum_of_gas = list()
for index, row in df2.iterrows():
    wells_iter = 0
    oil_iter, water_iter, gas_iter = 0, 0, 0
    for oil, water, gas in zip(row['WOPT'], row['WWPT'], row['WGPT']):
        if oil != 0 or gas != 0 or water != 0:
            wells_iter += 1
    work_wells.append(wells_iter)
df2['Work_wells'] = np.array(work_wells)
#df2['Sum_oil'] = df2['WOPT'].sum


df2.to_excel(r'/Users/yurabaronov/result_excel/econom.xlsx')
df.to_excel(r'/Users/yurabaronov/result_excel/all.xlsx')
