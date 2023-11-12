pressure = [135.00, 103.64, 92.84, 86.52, 82.13, 78.81, 76.16, 73.97, 72.11, 70.5]

def step(x1, x2, count):
    step = (x1 - x2) / 7
    #print(x1)
    for i in range(0, 7):
        print("%.2f" % (x1 - step))
        x1 = x1 - step
        count += 1
    #print("------")
    return count

count = 0
print(pressure[0])
for i in range(0, len(pressure) - 1):
    count = step(pressure[i], pressure[i + 1], count)
