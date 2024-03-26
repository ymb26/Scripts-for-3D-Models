from dateutil.relativedelta import relativedelta
import datetime
from datetime import datetime
from collections import Counter

file_out = open(r'C:\1\Rewrite\sch_jun-oct.txt', 'w')

start_date = datetime.strptime("26.06.2023", "%d.%m.%Y")
three_month_date = datetime.strptime("16.10.2023", "%d.%m.%Y")
two_years_date = start_date + relativedelta(years=2)
end_date = start_date + relativedelta(years=26)

count = 0

while start_date <= three_month_date:
    file_out.write("DATES\n")
    file_out.write("%d %s %d /\n/\n" % (start_date.day, start_date.strftime("%B").upper()[:3], start_date.year))
    #file_out.write("TSTEP\n")
    #file_out.write("0.001\t/\n")
    #file_out.write("/\n")
    print("DATES")
    print("%d %s %d /\n/\n" % (start_date.day, start_date.strftime("%B").upper()[:3], start_date.year))
    start_date += relativedelta(days=1)
    count += 1
print(count)

