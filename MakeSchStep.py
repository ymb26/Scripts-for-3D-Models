from dateutil.relativedelta import relativedelta
import datetime
from datetime import datetime
from collections import Counter

file_out = open(r'Y:\MVR_ORENBURG\4_iter\timestep_25year.txt', 'w')

start_date = datetime.strptime("01.01.2024", "%d.%m.%Y")
three_month_date = datetime.strptime("01.11.2026", "%d.%m.%Y")
two_years_date = start_date + relativedelta(years=2)
end_date = start_date + relativedelta(years=26)

#end_date = datetime.strptime("01.01.2050", "%d.%m.%Y")
count = 0
'''
while start_date < three_month_date:
    file_out.write("DATES\n")
    file_out.write("%d %s %d /\n/\n" % (start_date.day, start_date.strftime("%B").upper()[:3], start_date.year))
    print("DATES")
    print("%d %s %d /\n/\n" % (start_date.day, start_date.strftime("%B").upper()[:3], start_date.year))
    start_date += relativedelta(days=1)
    
'''
while start_date < two_years_date:
    if start_date.day == 1:
        file_out.write("DATES\n")
        file_out.write("%d %s %d /\n/\n" % (start_date.day, start_date.strftime("%B").upper()[:3], start_date.year))
        print("DATES")
        print("%d %s %d /\n/\n" % (start_date.day, start_date.strftime("%B").upper()[:3], start_date.year))
        start_date += relativedelta(months=1)

while start_date <= end_date:
    if start_date.day == 1:
        file_out.write("DATES\n")
        file_out.write("%d %s %d /\n/\n" % (start_date.day, start_date.strftime("%B").upper()[:3], start_date.year))
        print("DATES")
        print("%d %s %d /\n/\n" % (start_date.day, start_date.strftime("%B").upper()[:3], start_date.year))

        ##add november
        file_out.write("DATES\n")
        file_out.write("%d %s %d /\n/\n" % (start_date.day, "NOV", start_date.year))
        print("DATES")
        print("%d %s %d /\n/\n" % (start_date.day, start_date.strftime("%B").upper()[:3], start_date.year))

    start_date += relativedelta(years=1)
