import os
from datetime import datetime


#file_path = r'Z:\Baronov\ORENBURG_MVR\4_iter\6_optimal\7'

count = 1
count_file = 1
folder_path = r'Y:\MVR_ORENBURG\Result_6_peak\7'

for root, dirs, files in os.walk(folder_path):
    feature_of_name = "3_sector"
    #print(dirs)
    if feature_of_name in root:
        casename = os.path.join(root) + "\\" + "log.txt"  ## rfind('\\')
        file = open(casename, 'r')
        for line in reversed(file.readlines()):
            if "time:" in line and "]" in line:
                #timed = datetime.strptime(line[line.rfind("[")+1:-2], '%d %B %Y').strftime('%d-%m-%Y')
                print(casename[casename.rfind("3_sector")+9:casename.rfind("\\")-5], datetime.strptime(line[line.rfind("[")+1:-2], '%d %b %Y').strftime('%d-%m-%Y'), sep='\t')
                #print(casename, timed)
                break
        #print(casename)
        count += 1
        #break
