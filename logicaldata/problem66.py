data1 = [10, 20, 30, 40, 50]
data2 = [30, 40, 50, 60, 70]

common = []

for item in data1:
    if item in data2:
        common.append(item)

print("Common data:", common)