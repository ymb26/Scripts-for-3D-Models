import pandas as pd


for count in range(0, 44):
    try:
        path = r'C:\1\4_Scripts\faults_sticks\base\Fault_interpretation_%s_(Depth_1)' % count
        path_out = r'C:\1\4_Scripts\faults_sticks\result_0\Fault_%s.txt' % count
        df = pd.read_csv(path, sep='[ ]+', header=None, engine='python')
        df[8] = 0.0
        df[9] = 0.0
        df[10] = "--"
        df = df.drop_duplicates(subset=[7])
        print(df[10])
        #df[[3, 4, 7]].to_csv(path_out, index=False, header=False)

        with open(path_out, 'w') as f:
            f.write("FAULT\n")
        df.to_csv(path_out, mode='a', index=False, columns=[3, 4, 8, 9, 10, 7], header=False, sep=' ')

        with open(path_out, 'a') as f:
            f.write("/\n")
    except:
        print(count, " - wrong")