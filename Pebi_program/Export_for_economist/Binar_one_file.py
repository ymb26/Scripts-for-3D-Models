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
def binaryProcessing(casename, rdata_path):

    ##global begin_date
    df, wells_list = get_tab_from_bin(casename)
    #df.to_excel(r'C:\1\4_Scripts\Test_econom\10_1.xlsx')
    wells_array = [b'1', b'2', b'3']  ##well list
    wells_array_str = list()  ##well list - byte to str
    for well in wells_array:
        wells_array_str.append(well.decode('utf-8'))
    list_of_params = [b'WOPT', b'WWPT', b'WGPT', b'WIT', b'WOPR', b'WWPR', b'WGPR', b'WWCT', b'WBHP']


    arrays = [[], []]
    useless_wells_byte = list(set(wells_list) - set(wells_array))
    useless_wells_str = list()
    for well in useless_wells_byte:
        useless_wells_str.append(well.decode('utf-8'))
    list_of_params = [x for x in list_of_params if x in df]
    df2 = df[list_of_params]
    df2 = df2.rename(columns={b'WOPT': 'WOPT', b'WWPT': 'WWPT', b'WGPT': 'WGPT', b'WIT': 'WIT', b'WOPR': 'WOPR', b'WWPR': 'WWPR', b'WGPR':'WGPR', b'WWCT': 'WWCT', b'WBHP': 'WBHP'})

    df2 = df2.rename(columns={b'SM3': str('SM3')})
    df2 = df2.rename(columns={b'SM3/DAY': str('SM3/DAY')})
    df2 = df2.rename(columns={b'BARSA': str('BARSA')})
    df2 = df2.rename(columns={b'': str()})
    for well, well1 in zip(wells_array, wells_array_str):
        df2 = df2.rename(columns={well: "Well " + well1})
    for well, well1 in zip(useless_wells_byte, useless_wells_str):
        df2 = df2.rename(columns={well: well1})
    for well in useless_wells_str:
        try:
            df2 = df2.drop(columns=well, level=1)
        except:
            continue
    #df2['Timesteps'] = df['DAYS']
    #df2['Times'] = df[b'TIME']
    df2.insert(0, 'Times', df[b'TIME'])
    df2.insert(0, 'Timesteps', df['DAYS'])
    file = open(rdata_path, 'r').readlines()
    for i in range(len(file)):
        if "START" in file[i]:
            start_date_str = file[i + 1][:file[i+1].find("/")].strip()
            break
    start_date = datetime.strptime(start_date_str, "%d %b %Y")
    time_array = [start_date + timedelta(days=step) for step in df2['Times']]
    #df2['Date'] = np.array(time_array)
    df2.insert(0, 'Date', np.array(time_array))

    df['Date'] = df2['Date']


    work_wells = list()
    flag = 0
    for idx, row in df2.iterrows():
        wells_iter = 0
        for oil, water, gas, day in zip(row['WOPT'], row['WWPT'], row['WGPT'], row['Date']):   #no WIT
            if oil != 0 or gas != 0 or water != 0:
                wells_iter += 1
            if oil != 0 and flag == 0:
                begin_date = df2['Date'].iloc[idx - 1]  # start data rate - (example start - 01.01.2023 q = 0)
                flag = 1
        work_wells.append(wells_iter)
    #df2['Work_wells'] = np.array(work_wells)

    for p, total in zip(list_of_params, ['Total oil', 'Total water', 'Total gas']):
        df2[total] = df2[p.decode('utf-8')].sum(axis=1)

    df3 = pd.DataFrame()
    df3.insert(0, 'Total gas', df2['WGPT']['Well 2'])
    df3.insert(0, 'Total water', df2['WWPT']['Well 2'])
    df3.insert(0, 'Total oil', df2['WOPT']['Well 2'])
    df3.insert(0, 'Date', df2['Date'])



    output_df = pd.DataFrame()

    for i in range(0, 11):
        #xxx = df2.loc[df2['Date'] == begin_date + relativedelta(years=i), ['Total oil', 'Total water', 'Total gas']]    ##when start well
        xxx = df2.loc[df2['Date'] == start_date + relativedelta(years=i), ['Total oil', 'Total water', 'Total gas', 'Date']]    ##when start model
        output_df = pd.concat([output_df, xxx], axis=0, ignore_index=True)
    output_df = output_df.droplevel([0, 1, 2], axis=1)
    output_df.columns = ['Total oil', 'Total water', 'Total gas', 'Date']
    output_df.loc[0, 'Date'] = begin_date
    output_df['Step'] = output_df['Date'].diff()
    output_df['Diff oil'] = output_df['Total oil'].diff() / output_df['Step'].dt.days
    output_df['Diff water'] = output_df['Total water'].diff() / output_df['Step'].dt.days
    output_df['Diff liquid'] = output_df['Diff water'] + output_df['Diff oil']
    output_df['Diff gas'] = output_df['Total gas'].diff() / output_df['Step'].dt.days
    for i in range(43):
        output_df.loc[len(output_df.index)] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    output_df = output_df.fillna(0)



    #print(output_df.loc['Diff oil'])
    #df_all = pd.concat(df_all, output_df.loc['Diff oil'], axis=0)
    ####################


    yyy = list()
    for col in output_df.columns:
        yyy.append(output_df[col].to_string(index=True).split())
    years_array = [i for i in range(2022, 2076)]
    yyy2 = [a for b in yyy for a in b]

    print(df)
    return df, df2



if __name__ == "__main__":
    #trushko = [r'C:\1\1_Field\Multi_var_2\Big_data_result\L_500_125_standart_15_only_two_0000',
    #           r'C:\1\1_Field\Multi_var_2\Big_data_result\L_600_150_hybrid_12_only_two_well_0000',
    #           r'C:\1\1_Field\Multi_var_2\Big_data_result\L_500_125_stPAA_15_only_two_0000']
    #path = r'C:\1\1_Field\Multi_var_2\23_MVR_copy\L_500_125_standart_15_only_two_0000'  ## #1
    #path = r'C:\1\1_Field\Multi_var_2\24_MVR_600_m\L_600_175_hybrid_12_only_two_0000'  ## #2
    #for path in trushko:
    #    casename = r'%s\%s' % (path, path[path.rfind('\\')+1:-5])
     #   df, df2 = binaryProcessing(casename, casename + ".rdata")
      #  print(casename)
        #with pd.ExcelWriter(r'C:\1\4_Scripts\Big_export_SPD\Trushko_3_vars\3_wells_binar_export.xlsx', mode='a', if_sheet_exists='replace') as writer:
        #    df.to_excel(writer, sheet_name=path[path.rfind('\\')+1:-5])

        #with pd.ExcelWriter(r'C:\Users\baronov.ym\Desktop\Add_after_copy_mvr_from_server\7_PPD\PPD2.xlsx') as writer2:  ##, mode='a', if_sheet_exists='replace'
        #    df2.to_excel(writer2, sheet_name=path[path.rfind('\\')+1:-5])
    path = r'Z:\Baronov\Trushko_MVR\600\L_600_150_hybrid_12_without_degr_0000'
    casename = r'%s\%s' % (path, path[path.rfind('\\') + 1:-5])
    df, df2 = binaryProcessing(casename, casename + ".rdata")
    with pd.ExcelWriter(r'Z:\Baronov\Trushko_MVR\L_600_150_hybrid_12_without_degr.xlsx') as writer2:  ##, mode='a', if_sheet_exists='replace'
        df2.to_excel(writer2, sheet_name=path[path.rfind('\\') + 1:-5])
    with pd.ExcelWriter(r'Z:\Baronov\Trushko_MVR\L_600_150_hybrid_12_without_degr_binar.xlsx') as writer:
        df.to_excel(writer, sheet_name=path[path.rfind('\\')+1:-5])
#df3.to_excel(r'C:\1\4_Scripts\Big_export_SPD\Trushko_3_vars\3_wells.xlsx')



    #df2.to_excel(writer, sheet_name=casename[casename.rfind("\\L_") + 1:])
    #df_all.to_excel(r'C:\1\4_Scripts\Test_econom\additional_cases\econom.xlsx', index='1')

