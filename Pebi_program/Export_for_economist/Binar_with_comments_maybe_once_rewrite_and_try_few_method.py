import struct
import codecs
import os
import numpy as np
import pandas as pd
import openpyxl
from openpyxl.chart import Reference, BarChart, LineChart
import io
from datetime import datetime
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta

from pylab import plt
import matplotlib.colors as colors

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
                break
            else:
                _, name, datalen, type = unpack('>L8sL4s', head)  # size = calcsize('>L8cL4c')
                name = name.strip()
                if datalen == 0:
                    break
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
                    m = array(m, dtype=npfmt)
                    if name not in data:
                        data[name] = [m]
                    else:
                        data[name] += [m]
    return data


def get_tab_from_bin(casename):
    from numpy import array, compress, where
    from datetime import date
    from pandas import DataFrame, to_datetime

    def list_strip(lst):
        return list(map(lambda x: x.strip(), spec[lst][0]))

    spec = read_bin(casename + '.SMSPEC')  # Summary specification file
    start_date = spec.get(b'STARTDAT')
    kw, kn, un = list(map(list_strip, (b'KEYWORDS', b'WGNAMES', b'UNITS')))
    wells_list = list(set(kn) - set((b':+:+:+:+',)))
    cols = [kw, kn, spec[b'NUMS'][0], un]  # 'NUMS' = CELL | REGION NUMBER
    unsmry = read_bin(casename + '.UNSMRY')  # Unified summary file
    df = DataFrame(array(unsmry[b'PARAMS']), columns=cols)
    del unsmry
    df.index.names, df.columns.names = ['date'], ['keyword', 'wgname', 'num', 'unit']
    df = df.T.drop_duplicates().T  # WBHP duplicated in output
    s = date(*start_date[0][::-1])
    df.index = [s + timedelta(value) for index, value in df[b'TIME'].itertuples()]

    return df, wells_list

def binaryProcessing(casename, output_path):
    import datetime

    df, wells_list = get_tab_from_bin(casename)
    df_all = pd.DataFrame()

    print(wells_list)

    with pd.ExcelWriter(output_path) as writer:    ##, mode='a', if_sheet_exists='replace'
        #list of vector
        #list_of_vectors = [b'WOPR']
        #wells_list.remove(b'FIELD')
        #wells_list.remove(b'G')
        ### chose if you want export all wells in sheets
        '''
        for elem in sorted(wells_list):
            try:
                df.xs(elem, level="wgname", axis=1, drop_level=False).to_excel(writer, sheet_name=elem)
            except:
                print(elem)
        '''
        #'''
        wells_list.remove(b'FIELD')
        wells_list.remove(b'1568G')
        wells_list.remove(b'1575G')
        wells_list.remove(b'G')
        data_list = [datetime.date(2023, 1, 1), datetime.date(2024, 1, 1), datetime.date(2025, 1, 1), datetime.date(2026, 1, 1), datetime.date(2027, 1, 1), datetime.date(2028, 1, 1),
                     datetime.date(2029, 1, 1), datetime.date(2030, 1, 1), datetime.date(2031, 1, 1), datetime.date(2032, 1, 1), datetime.date(2033, 1, 1), datetime.date(2034, 1, 1)]
        for elem in sorted(wells_list):
            #print(df.xs(elem, level="wgname", axis=1, drop_level=False)[[b'WOPT', b'WWPT']].loc[data_list])
            
            for idx, row in df.xs(elem, level="wgname", axis=1, drop_level=False).iterrows():
                if row[b'WOPT'][0] != 0:
                    #print(key)
                    break
                else:
                    key = idx
            df2 = df.xs(elem, level="wgname", axis=1, drop_level=False)[[b'WOPT', b'WWPT', b'WGPT']].loc[data_list]
            df2[b'WLPT'] = df2[b'WOPT'] + df2[b'WWPT']
            wip_days = []
            for idx, row in df2.iterrows():

                if idx - key < timedelta(days=0):
                    #print(idx - key)
                    wip_days.append(timedelta(days=0))
                elif idx - key < timedelta(days=365):
                    wip_days.append(idx - key)
                else:
                    wip_days.append(idx - last_idx)
                last_idx = idx

            #df2 = df2.drop(columns=b'WOPT', level=1)
            df2.columns = df2.columns.droplevel(level=1)
            df2.columns = df2.columns.droplevel(level=1)
            df2.columns = df2.columns.droplevel(level=1)
            #print(df2)
            df2['Days'] = np.array(wip_days)
            df2['Step'] = df2['Days'].dt.days.astype('int32')
            df2 = df2.fillna(0)
            #print(df2['Step'])
            #print(df2[b'WOPT'] / df2[b'WWPT'] / int(365))
            df3 = df2[[b'WOPT', b'WWPT', b'WLPT', b'WGPT']].diff()
            df3[b'WOPT'] = df3[b'WOPT'] / 365.25        #df2['Step']
            df3[b'WWPT'] = df3[b'WWPT'] / 365.25        #df2['Step']
            df3[b'WLPT'] = df3[b'WLPT'] / 365.25        #df2['Step']
            df3[b'WGPT'] = df3[b'WGPT'] / 365.25 / 1000 #df2['Step'] / 1000
            #df3['Work Days'] = df2['Step']
            df3 = df3.fillna(0)
            df3 = df3.T
            for i in range(11):
                df3 = df3._append(pd.Series([np.nan], name=""))
            #df_all = pd.concat([df_all, [np.nan]], axis=0)
            df3 = pd.concat([df3], keys=[elem, elem], names=['Well'])

            df_all = pd.concat([df_all, df3], axis=0)
            print(df_all)
        df_all.to_excel(writer)
        #'''

if __name__ == "__main__":
    #output_path = r'Y:\Baronov\L_700_150_hybrid_12_pebi2.xlsx'
    #casename = r'Y:\Baronov\MVR_true_frac\MVR_base\L_700_150_hybrid_12_0000\L_700_150_hybrid_12'

    output_path = r'C:\1\KP707_700_6_wells_false_spd.xlsx'
    #casename = r'Y:\Baronov\Base_without_frac\ADAPT_31_v3_for_prognoz_v1_0000\ADAPT_31_v3_for_prognoz_v1'
    casename = r'Y:\Baronov\30_MVR_kust_6_wells\KP707_700_6_wells_false_0002\KP707_700_6_wells_false'

binaryProcessing(casename, output_path)

