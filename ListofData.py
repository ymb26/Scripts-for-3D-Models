import os

path_in = r'C:\1\1_Field\Multi_var_2\23_MVR'

count = 1
for root, dirs, files in os.walk(path_in):
    for file in files:
        if file.endswith(".data"):
            print(count, file)
            count += 1