import os

###### Раздел - что меняется (2 параметра - 2 папки)
##############################################################################
###вставить путь с датниками - папка с датниками
###пример - Y:\MVR_ORENBURG\7_iter_check_frac\Datafiles

path_in = r'Y:\MVR_ORENBURG\7_iter_check_frac\Datafiles'

###вставить путь - куда положить запускающий бат-файл
###пример - Y:\MVR_ORENBURG\7_iter_check_frac\Datafiles

path_out = r'C:\Users\baronov.ym\PycharmProjects\Scripts-for-3D-Models'



##############################################################################
###### - здесь лучше ничего не трогать
####program
with open(path_out + "\\start.bat", 'w') as out_file:   ##здесь создается бат-файл для запуска
    count = 1
    for root, dirs, files in os.walk(path_in):  ## здесь по очереди находятся все датники и записываются в бат-файл
        for file in files:
            if file.endswith(".data"):
                print(file)
                out_file.write("START\t")
                out_file.write("xxx\t")
                out_file.write(path_in + "\\" + file)
                out_file.write('\n')
                count += 1
###end