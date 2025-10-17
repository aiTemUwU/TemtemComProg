numList, sumPos = [float(e) for e in input().split()], int(input())
sumDict = {}

rotList = numList

for i in range(0, len(numList)):
	rotList[:] = [rotList[-1]] + rotList[0:len(rotList)-1]
	sumDict.update({sum(rotList[0:sumPos]):rotList[0:sumPos]})

maxSum = max(sumDict.keys())
maxRotList = sumDict.get(maxSum)

print(round(maxSum, 2))
print(maxRotList)