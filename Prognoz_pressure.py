from datetime import datetime
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta

wells = ["22101", "22106", "22111", "22127", "22137", "42929", "42962", "42963", "42964", "42965", "42966", "42967", "42968", "43723", "43724", "21501", "22102", "22103", "22104", "22105", "22108", "22109", "22110", "22155ST2", "42930G", "42931G", "42932G", "42933G", "42934G", "42935G", "42936G", "42958G", "42959G", "42960G", "43785G"]
dates = ["27.12.2022", "03.06.2022", "22.07.2022", "08.12.2022", "11.09.2022", "23.05.2021", "03.03.2023", "29.01.2023", "11.01.2023", "12.10.2022", "30.11.2022", "30.11.2022", "30.11.2022", "28.08.2021", "23.08.2021", "26.09.2022", "13.02.2022", "27.01.2022", "01.02.2022", "28.03.2022", "15.02.2023", "23.03.2023", "30.11.2022", "01.04.2023", "10.06.2021", "17.07.2021", "21.09.2021", "17.11.2021", "26.12.2021", "11.04.2022", "26.04.2022", "21.04.2022", "18.08.2022", "31.05.2022", "19.01.2023"]
pressures = [124.9521561, 96.65377808, 40, 40, 204.2450104, 92.80039978, 162.8215179, 137.6919708, 58.37256241, 192.7380524, 131.3585205, 134.7818146, 82.91693878, 213.4034119, 119.3003464, 93.30368805, 98.42136383, 77.13788605, 138.807251, 108.2489243, 130.151535, 166.0545044, 125.1891403, 143.983551, 141.2476807, 133.807373, 77.93759918, 161.8291016, 168.6804047, 170.2246094, 149.9990387, 146.9663544, 129.3565369, 0, 129.3565369]
limit_pressure = 100
file_out = open(r'C:\1\1_Field\%s.txt' % limit_pressure, 'w')
for w, d, p in zip(wells, dates, pressures):
    new_d = datetime.strptime(d, "%d.%m.%Y")
    if p > limit_pressure:
        while p > limit_pressure:
            print(w, new_d, "OPEN\tPROD\tBHPT\t", "{:.5f}".format(p))
            file_out.write(w + '\t' + str(new_d) + "\tOPEN\tPROD\tBHPT\t" + "{:.5f}".format(p) + '\n')
            #new_d = new_d + relativedelta(months=1, day=new_d.day)
            new_d = new_d + relativedelta(days=1)
            p -= 0.06452
        print(w, new_d, "OPEN\tPROD\tBHPT\t", limit_pressure)
        file_out.write(w + '\t' + str(new_d) + "\tOPEN\tPROD\tBHPT\t" + str(limit_pressure) + '\n')
    elif p < 2:
        continue
    else:
        print(w, new_d, "OPEN\tPROD\tBHPT\t", "{:.5f}".format(p - 2))
        file_out.write(w + '\t' + str(new_d) + "\tOPEN\tPROD\tBHPT\t" + "{:.5f}".format(p - 2) + '\n')

