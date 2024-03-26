import pandas as pd
from dateutil.relativedelta import relativedelta
import datetime
from datetime import datetime
from collections import Counter

start = ["22.06.2017", "29.07.2017", "15.11.2017", "01.08.2018", "06.09.2018", "15.03.2019"]
end = ["01.07.2017", "07.10.2017", "24.01.2018", "06.08.2018", "27.12.2018", "22.04.2019"]

#start = ["02.11.2019"]
#end = ["09.11.2019"]







start_date = list()
end_date = list()

for s in start:
    start_date.append(datetime.strptime(s, "%d.%m.%Y"))
for e in end:
    end_date.append(datetime.strptime(e, "%d.%m.%Y"))

for s, e in zip(start_date, end_date):
    while s != e:
        print(s.strftime("%d.%m.%Y"))
        s += relativedelta(days=1)
    #break


