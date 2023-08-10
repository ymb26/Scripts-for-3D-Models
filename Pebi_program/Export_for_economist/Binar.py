import struct
import codecs
import os
import numpy as np
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
def binaryProcessing(df_all, casename, rdata_path):

    ##global begin_date
    df, wells_list = get_tab_from_bin(casename)
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

    '''
    yyy = list()
    for col in output_df.columns:
        yyy.append(output_df[col].to_string(index=True).split())
    years_array = [i for i in range(2022, 2076)]
    yyy2 = [a for b in yyy for a in b]
    df_all = df_all._append(pd.DataFrame(output_df['Diff oil'].values, index=years_array, columns=["%s" % casename[casename.rfind("\\4_")+3:]]).T)
    df_all = df_all._append(
        pd.DataFrame(output_df['Diff water'].values, index=years_array, columns=["%s" % casename[casename.rfind("\\4_") + 3:]]).T)
    df_all = df_all._append(
        pd.DataFrame(output_df['Diff liquid'].values, index=years_array, columns=["%s" % casename[casename.rfind("\\4_") + 3:]]).T)
    df_all = df_all._append(
        pd.DataFrame(output_df['Diff gas'].values, index=years_array, columns=["%s" % casename[casename.rfind("\\4_") + 3:]]).T)


    for i in range(8):
        df_all = df_all._append(pd.Series([np.nan], name="%s" %casename[casename.rfind("\\L_") + 3:]))
    df_all = df_all._append(pd.Series([np.nan], name=""))
    df_all = df_all._append(pd.Series([np.nan], name=""))
    '''
    #print(df_all)
    return df_all, df2



if __name__ == "__main__":
    df_all = pd.DataFrame()
    path_folder_mvr = r'C:\1\1_Field\Multi_var_2\23_MVR_2_case'
    #path_folder_mvr = r'C:\1\1_Field\Multi_var_2\23_MVR_2_case'
    count = 1
    with pd.ExcelWriter(r'C:\1\4_Scripts\Test_econom\PPD\nadd.xlsx', engine="openpyxl") as writer:
        for root, dirs, files in os.walk(path_folder_mvr):
            feature_of_name = "6_PPD_longitudinal_recu_schedule_no_PPD_0000"  ## change on what you search
            if feature_of_name in root:
                casename = os.path.join(root) + "\\" + os.path.join(root)[os.path.join(root).rfind("\\6_"):-5]    ## rfind('\\')
                print(casename)
                df_all, df2 = binaryProcessing(df_all, casename, casename + ".rdata")
                df2.to_excel(writer, sheet_name=casename[casename.rfind("\\6_") + 1:])
            #df_all.to_excel(r'C:\1\4_Scripts\Test_econom\PPD\econom.xlsx', index='1')

