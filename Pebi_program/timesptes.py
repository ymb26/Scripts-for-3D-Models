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

array = ["31.05.2024", "17.06.2024", "04.07.2024", "21.07.2024", "07.09.2024", "24.09.2024", "11.10.2024", "28.10.2024", "14.12.2024", "31.12.2024", "17.01.2025", "03.02.2025", "22.03.2025", "08.04.2025", "25.04.2025", "12.05.2025", "29.06.2025", "16.07.2025", "02.08.2025", "19.08.2025", "05.10.2025", "22.10.2025", "08.11.2025", "25.11.2025", "12.01.2026", "29.01.2026", "15.02.2026", "04.03.2026", "21.03.2026"]
count = 1
for d in array:
    for i in range(0, 7):
        print(count, datetime.strptime(d, "%d.%m.%Y") + relativedelta(months=i, day=datetime.strptime(d, "%d.%m.%Y").day))
    count += 1