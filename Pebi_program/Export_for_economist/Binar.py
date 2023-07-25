import struct
import codecs
#from pylab import plt
import numpy as np
import matplotlib.colors as colors
import pandas as pd



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
    #df.to_csv("C:\\1\\test.xls", sep='\t')
    #print(df)
    df = df.T.drop_duplicates().T  # WBHP duplicated in output
    return df, wells_list


#casename = r'carbon\RESULTS\carb_v15l6p'

#casename = r'C:\1\1_Field\Р10-90_Oil_case\Р75\Data_P75_gmm50_0005\Data_P75_gmm50'
#casename = r'C:\1\1_Field\Multi_var_2\23_MVR\L_300_75_standart_15_0000\L_300_75_standart_15'
casename = r'/Users/yurabaronov/Desktop/PHYSGEO/test_model/L_300_75_standart_15_0000/L_300_75_standart_15'

df, wells_list = get_tab_from_bin(casename)
wells_array = [b'1', b'2', b'3']
list_of_params = [b'WOPT', b'WWPT', b'WGPT']
print(len(wells_array))
arrays = [[], []]
for param in list_of_params:
    for i in range(len(wells_array)):
        arrays[0].append(param)
        arrays[1].append(wells_array[i])
tuples = list(zip(*arrays))
print(tuples)
#pd.MultiIndex.from_product(tuples, names=["first", "second"])
#print(df)
for p in list_of_params:
    print(df[p][[b'1', b'2', b'3']])
df1 = pd.DataFrame
#df1['WWPT'] = df[b'WWPT']
#df1.insert(1, "WWPT", [123,23])
df1.insert(1, "newcol", [99, 99])


#for index, row in df.iterrows():
 #   print(row[b'WOPT'])

#df.to_excel(r'C:\1\4_Scripts\Test_econom\econom.xlsx')
