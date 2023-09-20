import os

for root, dirs, files in os.walk(os.getcwd()):
    if ".txt" in root:
        print(os.path.join(root))
    file = open('test1.txt', 'w')
    file.close()
