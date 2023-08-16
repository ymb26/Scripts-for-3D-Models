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

def binaryProcessing(casename):
    df, wells_list = get_tab_from_bin(casename)
    with pd.ExcelWriter(r'C:\1\4_Scripts\Test_econom\Export_wells.xlsx') as writer:
        for elem in sorted(wells_list):
            print(df.xs(elem, level="wgname", axis=1, drop_level=False))
            df.xs(elem, level="wgname", axis=1, drop_level=False).to_excel(writer, sheet_name=elem)
    #df.to_excel(r'C:\1\4_Scripts\Test_econom\1.xlsx')


if __name__ == "__main__":
    casename = r'C:\1\1_Field\Multi_var_2\24_MVR_600_m\L_600_75_hybrid_12_0000\L_600_75_hybrid_12'
    binaryProcessing(casename)



    #df2.to_excel(writer, sheet_name=casename[casename.rfind("\\L_") + 1:])
    #df_all.to_excel(r'C:\1\4_Scripts\Test_econom\additional_cases\econom.xlsx', index='1')

