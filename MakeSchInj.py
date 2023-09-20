#"DATES\n" + str(row['DD.MM.YYYY'].day) + ' ' + str(row['DD.MM.YYYY'].strftime("%B").upper()[:3]) + ' ' + str(row['DD.MM.YYYY'].year) + "\t/\n/\n")

import pandas as pd
from dateutil.relativedelta import relativedelta
import datetime
from datetime import datetime
from collections import Counter

wells_ppd = ["43724", "42934G", "22102G", "22105G", "42935G", "42960G", "42937BGS", "22137", "21501G", "22110G", "22127", "42964", "22108G", "22126", "21602G", "22115G", "22157", "POZ-4", "22129", "21607G", "21605G", "22001", "22114G", "POZ-9", "21606G", "22113G", "POZ-7", "21611G", "22006", "22120", "22122", "21612G", "21615G", "22126G", "22005", "21617G", "22121G", "22011", "21619G", "22012", "21620G", "22138", "22013", "22015", "22143", "22016", "22140", "22133", "22018", "22020", "22132", "22144", "22023", "22037", "22024", "22027", "22131", "22130", "22040", "22029", "22030", "22033", "22036", "22035", "22038", "22021"]
date_ppd = ["22.08.2024", "25.12.2024", "13.02.2025", "28.03.2025", "10.04.2025", "30.05.2025", "27.08.2025", "11.09.2025", "25.09.2025", "26.10.2025", "08.12.2025", "10.01.2026", "15.02.2026", "03.07.2026", "06.07.2026", "09.08.2026", "16.08.2026", "10.09.2026", "20.09.2026", "11.11.2026", "28.12.2026", "07.01.2027", "13.01.2027", "20.01.2027", "05.02.2027", "23.02.2027", "18.04.2027", "14.05.2027", "12.06.2027", "27.06.2027", "20.09.2027", "30.09.2027", "24.01.2028", "23.02.2028", "27.02.2028", "03.05.2028", "28.07.2028", "01.08.2028", "11.08.2028", "22.09.2028", "30.09.2028", "09.11.2028", "13.11.2028", "04.01.2029", "21.02.2029", "25.02.2029", "14.04.2029", "05.06.2029", "09.06.2029", "21.09.2029", "08.11.2029", "30.12.2029", "03.01.2030", "24.02.2030", "08.06.2030", "30.07.2030", "16.09.2030", "07.11.2030", "02.01.2031", "16.04.2031", "19.09.2031", "22.02.2032", "05.06.2032", "27.07.2032", "08.11.2032", "30.12.2032"]
date_ppd_time = list()
dict_ppd = dict()
for d in date_ppd:
    date_ppd_time.append(datetime.strptime(d, "%d.%m.%Y"))


path_out = r'C:\1\Schedule_inje_all_kusts_month_step.txt'
file_out = open(path_out, 'w')

def FindDuplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


start_date = datetime.strptime("01.01.2021", "%d.%m.%Y")
end_date = datetime.strptime("01.01.2050", "%d.%m.%Y")
count = 0
counter = Counter(date_ppd)
repeated_elements = [item for item, count in counter.items() if count > 1]
if len(repeated_elements) > 0:
    print("REPEAT - ", repeated_elements)
while start_date <= end_date:
    if start_date.day == 1:
        file_out.write("DATES\n")
        file_out.write("%d %s %d /\n/\n" % (start_date.day, start_date.strftime("%B").upper()[:3], start_date.year))
    if start_date in date_ppd_time:
        if start_date.day != 1:
            file_out.write("DATES\n")
            file_out.write("%d %s %d /\n/\n" % (start_date.day, start_date.strftime("%B").upper()[:3], start_date.year))
        file_out.write("WCONINJE\n")
        for index in FindDuplicates(date_ppd_time, start_date):
            file_out.write(wells_ppd[index])
            file_out.write(" WATER OPEN BHP 1* 1* 400 /\n")
        file_out.write("/\n")
        count += 1
    start_date += relativedelta(days=1)

file_out.close()
