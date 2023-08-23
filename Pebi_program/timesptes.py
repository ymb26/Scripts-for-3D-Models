import datetime
from datetime import datetime
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
'''
start_date = datetime.datetime(2024, 5, 31)
end_date = start_date + relativedelta(years=25)
current_time = start_date

month_export_date = datetime.datetime(2026, 1, 1)
print(end_date, start_date)
i = 0
while current_time < end_date:
    if current_time < month_export_date:
        current_time = current_time + relativedelta(months=1, day=1)
    else:
        current_time = current_time + relativedelta(years=1, day=1)
    print(current_time)
'''
'''
array = ["31.05.2024", "17.06.2024", "04.07.2024", "21.07.2024", "07.09.2024", "24.09.2024", "11.10.2024", "28.10.2024", "14.12.2024", "31.12.2024", "17.01.2025", "03.02.2025", "22.03.2025", "08.04.2025", "25.04.2025", "12.05.2025", "29.06.2025", "16.07.2025", "02.08.2025", "19.08.2025", "05.10.2025", "22.10.2025", "08.11.2025", "25.11.2025", "12.01.2026", "29.01.2026", "15.02.2026", "04.03.2026", "21.03.2026"]
count = 1
for d in array:
    for i in range(0, 7):
        print(count, datetime.strptime(d, "%d.%m.%Y") + relativedelta(months=i, day=datetime.strptime(d, "%d.%m.%Y").day))
    count += 1
'''

dict = {22157: "13.11.2034",
    22129: "27.01.2042",
    22008: "22.09.2030",
    22007: "13.11.2030",
    22006: "04.01.2031",
    22002: "25.02.2031",
    22004: "18.04.2031",
    22014: "09.06.2031",
    22005: "30.01.2032",
    22009: "26.01.2027",
    22010: "27.03.2027",
    22011: "10.09.2027",
    22012: "29.03.2028",
    22013: "14.02.2028",
    22015: "09.08.2028",
    22016: "20.10.2028",
    22017: "29.03.2028",
    22018: "14.02.2028",
    22019: "09.08.2028",
    22020: "20.10.2028",
    22029: "26.07.2039",
    22030: "21.02.2034",
    22031: "14.04.2034",
    22032: "05.06.2034",
    22033: "18.09.2034",
    22034: "14.04.2035",
    22036: "17.09.2035",
    22022: "19.09.2029",
    22021: "15.04.2030",
    22042: "18.09.2030"}
dict2 = {22042: "18.09.2030"}
for keys in dict:
    pressure =
    for i in range(0, 4):
        print(keys, datetime.strptime(dict[keys], "%d.%m.%Y") + relativedelta(months=i, day=datetime.strptime(dict[keys], "%d.%m.%Y").day))
        pressure -=