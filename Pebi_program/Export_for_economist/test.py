import pandas as pd
import os

path = r'C:\1\1_Field\Multi_var_2\23_MVR'

for root, dirs, files in os.walk(path):
    for dir in dirs:
        print(os.path.join(root, dir))
