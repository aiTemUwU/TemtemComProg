scoreList = [float(i) for i in input().split()]
scoreList.sort()

finalScore = round((scoreList[1] + scoreList[2])/2, 2)
print(finalScore)
