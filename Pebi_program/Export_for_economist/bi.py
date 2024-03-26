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
        return list(map(lambda x: x.strip().decode('utf-8'), spec[lst][0]))

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
    df.index = [s + timedelta(value) for index, value in df['TIME'].itertuples()]

    return df, wells_list

def binaryProcessing(casename, output_path):
    import datetime

    df, wells_list = get_tab_from_bin(casename)
    df_all = pd.DataFrame()

    #wells_array = [b'1313G']
    #wells_array2 = list()
    #for well in wells_list:
    #    if well not in wells_array:
    #        wells_array2.append(well)
    return df
    #return df.drop(columns=wells_array2, level=1)


if __name__ == "__main__":
    output_path = r'C:\1\1_Field\export\3_sector_frac_k015_a0004_GELACID_Prop_20_Acid_150_gelacid_140_rate_8.xlsx'
    casename = r'Y:\MVR_ORENBURG\Result_6_peak\7\3_sector_frac_k015_a0004_GELACID_Prop_20_Acid_150_gelacid_140_rate_8_0000\3_sector_frac_k015_a0004_GELACID_Prop_20_Acid_150_gelacid_140_rate_8'
    #casename = r'C:\1\1_Field\FromSasha\model\e42\e4\result'
    df = binaryProcessing(casename, output_path)
    #df.drop(columns=['FIELD'], level=1).to_excel(output_path, sheet_name=casename[casename.rfind("\\") + 1:])
    df.drop(columns=['FIELD', '1317G', '3315G', '1534G', '1313G', '3308G', '3310G', '3398G', '1529G2', '6366G', '6367G', '1529G'], level=1).to_excel(output_path, sheet_name="GELACID_20_150_8")
    print(df)

    ######################################################### usefull
    #df.to_excel(r'C:\1\check2.xlsx')
    #print(df)
    #df.columns = df.columns.str.decode("utf-8")
    #print(df)


    #folder_path = r'Y:\Baronov\Priob_U_622_big_matrix'

    #'''
    #output_path = r'Y:\Baronov\Priob_U_622\first'



    '''
    count = 1
    count_file = 1
    folder_path = r'Y:\MVR_ORENBURG\4_iter\1_old_assignment\7'
    with pd.ExcelWriter(r'Y:\MVR_ORENBURG\2_iter\1313_fact.xlsx') as writer:
        for root, dirs, files in os.walk(folder_path):
            feature_of_name = "3_sector"
            #feature_of_name2 = "frac02"
            if feature_of_name in root:
                #casename = root[root.rfind("\\") + 1:root.rfind("_")]
                casename = os.path.join(root) + "\\" + os.path.join(root)[os.path.join(root).rfind("\\"):-5]  ## rfind('\\')
                #print(count, casename)
                df2 = binaryProcessing(casename, "xxx")
                #df2.to_excel(writer, sheet_name=casename[casename.rfind("\\")+1:])
                df2.to_excel(writer, sheet_name="D" + casename[casename.rfind("4_sector_frac")+13:])
                #df2.to_excel(writer, sheet_name="D" + casename[casename.rfind("k05_")+5:])
                #df2.to_excel(writer, sheet_name=str(count))
                print(casename)
                #df2.to_excel(writer, sheet_name="D" + casename[casename.rfind("1_sector_frac") + 13:casename.rfind("1_sector_frac") + 15] + casename[casename.rfind("_rate"):])

                #print(casename[casename.rfind("\\")+1:])
                count += 1

    '''

            #df2 = binaryProcessing(casename, "xxx")
            #rint(casename[casename.rfind("\\") + 20:])
            ##df2.to_excel(writer, sheet_name=casename[casename.rfind("\\") + 1:])
            #df2.to_excel(writer, sheet_name=casename[:10])
    #'''