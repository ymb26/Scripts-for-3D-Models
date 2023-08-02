import pandas as pd

df = pd.DataFrame({'A': [11, 21, 31],
                   'B': [12, 22, 32],
                   'C': [13, 23, 33]},
                  index=['ONE', 'TWO', 'THREE'])
list_x = [2023, 2024, 2025]
print(df)
df = df.set_axis(list_x, axis=0)
print(df)
#         A   B   C
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33