import os

for root, dirs, files in os.walk(r'Y:\Baronov\Priob_U_622_MVR_comb'):
    for file in files:
        if ".data" in file:
            print(root + "\\" + file)

