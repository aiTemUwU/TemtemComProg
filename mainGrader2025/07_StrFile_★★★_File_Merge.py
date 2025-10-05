file1, file2 = input().split()

data1 = []
data2 = []

file1 = open(file1, "r")
file2 = open(file2, "r")

if file1 != "":
    for line in file1:
        id, grade = line.split()
        year = id[0:2]
        faculty = id[-2::]

        data1.append([faculty, year, grade, id])
else: pass

if file2 != "":
    for line in file2:
        id, grade = line.split()
        year = id[0:2]
        faculty = id[-2::]

        data2.append([faculty, year, grade, id])
else: pass

file1.close()
file2.close()

mergedData = data1 + data2
mergedData = sorted(mergedData)

for i in range(0, len(mergedData)):
    print(f"{mergedData[i][3]} {mergedData[i][2]}")

'''
data1.txt
5831111121 2.50
6032222221 3.12
6133333321 3.20
6231111122 2.45
6232222222 3.23

data2.txt

data3.txt
5841111126 2.77
6042222226 2.44
6141111128 3.20
6232222228 3.99

data4.txt
5931111121 2.66
6132222221 2.12
6231111122 2.13

data5.txt
5841111121 2.77
6042222221 2.44
6141111128 3.20
6232222228 3.99
'''
