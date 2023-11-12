import os

path_in = r'Y:\MVR_ORENBURG\2_iter\5_portov'

count = 1
for root, dirs, files in os.walk(path_in):
    for file in files:
        if file.endswith(".data"):
            print(count, file)
            count += 1