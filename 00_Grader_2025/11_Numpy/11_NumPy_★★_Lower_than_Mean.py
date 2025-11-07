import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.zeros((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    stuID = data[:, 0]
    stuAvgScore = np.sum((data[:, 1:] * weight), axis = 1)
    mean = np.sum(stuAvgScore)/len(data)

    lowerThanMean = stuID[stuAvgScore < mean]
    if len(lowerThanMean) == 0: print("None")
    else:
        output = "".join((str(e) + ", ") for e in lowerThanMean)[:-2]
        print(output)

    return

exec(input().strip())