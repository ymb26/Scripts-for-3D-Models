from dateutil.relativedelta import relativedelta
import datetime
from datetime import datetime
from collections import Counter

#trend = [160.0, 121.9, 108.4, 101.0, 95.6, 91.7, 88.7, 86.1, 83.9, 82.0, 80.4, 78.9, 77.5, 76.3, 75.2, 74.2, 73.3, 72.4, 71.6, 70.9, 70.2, 69.5, 68.8, 68.2, 67.7, 67.1, 66.6, 66.1, 65.6, 65.2, 65.0]
#wells = ["6371G", "6372G", "6373G", "6374G", "6375G", "6365G", "6363G", "6362G", "6360G"]
#datestart = ["01.01.2024", "01.02.2024", "01.03.2024", "01.04.2024", "01.05.2024", "01.06.2024", "01.07.2024", "01.08.2024", "01.09.2024"]

#trend = [135, 130.52, 126.04, 121.56, 117.08, 112.6, 108.12, 103.64, 102.1, 100.55, 99.01, 97.47, 95.93, 94.38, 92.84, 91.94, 91.03, 90.13, 89.23, 88.33, 87.42, 86.52, 85.89, 85.27, 84.64, 84.01, 83.38, 82.76, 82.13, 81.66, 81.18, 80.71, 80.23, 79.76, 79.28, 78.81, 78.43, 78.05, 77.67, 77.3, 76.92, 76.54, 76.16, 75.85, 75.53, 75.22, 74.91, 74.6, 74.28, 73.97, 73.7, 73.44, 73.17, 72.91, 72.64, 72.38, 72.11, 71.88, 71.65, 71.42, 71.19, 70.96, 70.73, 70.5, 70]
#wells = ["6371G", "6372G", "6373G", "6374G", "6375G", "6365G", "6363G", "6362G", "6360G"]

#wells = ["6371G", "6373G", "6374G", "6375G", "6365G", "6362G", "6360G"]
#datestart = ["01.01.2024", "01.02.2024", "01.03.2024", "01.04.2024", "01.05.2024", "01.06.2024", "01.07.2024"]

#wells = ["6371G", "6373G", "6374G", "6375G", "6365G", "6362G", "6360G"]
#datestart = ["01.01.2024", "01.02.2024", "01.03.2024", "01.04.2024", "01.05.2024", "01.06.2024", "01.07.2024"]


##old trend with angle in graphs
#trend = [135, 130.52, 126.04, 121.56, 117.08, 112.6, 108.12, 103.64, 102.1, 100.55, 99.01, 97.47, 95.93, 94.38, 92.84, 91.94, 91.03, 90.13, 89.23, 88.33, 87.42, 86.52, 85.89, 85.27, 84.64, 84.01, 83.38, 82.76, 82.13, 81.66, 81.18, 80.71, 80.23, 79.76, 79.28, 78.81, 78.43, 78.05, 77.67, 77.3, 76.92, 76.54, 76.16, 75.85, 75.53, 75.22, 74.91, 74.6, 74.28, 73.97, 73.7, 73.44, 73.17, 72.91, 72.64, 72.38, 72.11, 71.88, 71.65, 71.42, 71.19, 70.96, 70.73, 70.5, 70]
trend = [130.0, 128.1, 126.2, 124.4, 122.7, 121.0, 119.3, 117.7, 116.2, 114.7, 113.2, 111.8, 110.4, 109.0, 107.7, 106.4, 105.2, 104.0, 102.8, 101.6, 100.5, 99.4, 98.3, 97.2, 96.2, 95.2, 94.2, 93.2, 92.3, 91.4, 90.5, 89.6, 88.7, 87.9, 87.0, 86.2, 85.4, 84.6, 83.9, 83.1, 82.4, 81.6, 80.9, 80.2, 79.6, 78.9, 78.2, 77.6, 76.9, 76.3, 75.7, 75.1, 74.5, 73.9, 73.3, 72.8, 72.2, 71.7, 71.1, 70.6, 70.1, 70.0]

##ввод по датам 9
#wells = ["6375G", "6360G", "6372G", "6362G", "6363G", "6371G", "6374G", "6373G", "6365G"]
#datestart = ["27.10.2025", "10.12.2025", "18.01.2026", "26.02.2026", "03.04.2026", "08.05.2026", "13.06.2026", "13.07.2026", "17.08.2026"]

##ввод по датам 7 скважин
#wells = ["6375G", "6360G", "6362G", "6371G", "6374G", "6373G", "6365G"]
#datestart = ["27.10.2025", "10.12.2025", "18.01.2026", "26.02.2026", "03.04.2026", "08.05.2026", "13.06.2026"]  #, "13.07.2026", "17.08.2026"]

##ввод по датам 6 скважин
#wells = ["6375G", "6360G", "6362G", "6371G", "6373G", "6365G"]
#datestart = ["27.10.2025", "10.12.2025", "18.01.2026", "26.02.2026", "03.04.2026", "08.05.2026"] #, "13.06.2026"]  #, "13.07.2026", "17.08.2026"]

##ввод по датам 4 скважин
wells = ["6360G", "6371G", "6373G", "6365G"]
datestart = ["27.10.2025", "10.12.2025", "18.01.2026", "26.02.2026"]#, "03.04.2026", "08.05.2026"] #, "13.06.2026"]  #, "13.07.2026", "17.08.2026"]



print(len(wells), len(datestart))

date_ppd_time = list()
for d in datestart:
    date_ppd_time.append(datetime.strptime(d, "%d.%m.%Y"))

for w, d in zip(wells, date_ppd_time):
    count = 0
    for i in trend:
        print(w, "\t", (d + relativedelta(days=count)).strftime("%d.%m.%Y"), "\tOPEN\tPROD\tBHPT\t", i)
        #start_date.day, start_date.strftime("%B").upper()[:3], start_date.year
        count += 1
    #print(count)