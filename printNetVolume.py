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

from pylab import plt
import matplotlib.colors as colors


#folder_path = r'C:\1\1_Field\GDM_South_Siuld\11_12_2023'
folder_path = r'C:\1\1_Field\GDM_South_Siuld\11_12_2023_NEW_CUBS\Ups'

count = 0
amount = 0
for root, dirs, files in os.walk(folder_path):
    feature_of_name = "WELL_"
    if feature_of_name in root:
        casename = os.path.join(root) #+ "\\" + os.path.join(root)[os.path.join(root).rfind("\\"):-5]  ## rfind('\\')
        #print(count, casename)
        tmp = "sum VOL*NTG = "
        file = open(casename + "\\log.txt", 'r')
        lines = file.readlines()
        print(casename[casename.rfind("\\")+1:-5])
        for line in lines:
            if tmp in line:
                amount += 1
                print(amount, line, end="")
            if "time iteration" in line:
                break
        #break
        #df2 = binaryProcessing(casename, "xxx")
        # df2 = binaryProcessing(root + "\\" + casename, "xxx")
        #df2.to_excel(writer, sheet_name=casename[casename.rfind("\\") + 1:])
        # print(casename[casename.rfind("\\")+1:])
        count += 1