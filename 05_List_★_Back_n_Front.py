firstSet, secondSet, thirdSet = [], [], []
altFirstSet, altSecondSet = [], []

firstSetNum = int(input())
for i in range(0, firstSetNum):
    firstSet.append(int(input()))

secondSet = [int(i) for i in input().split()]

if len(secondSet) == 1:
    if secondSet[0] == -1:
        secondSet, thirdSet = [], []
    else:
        thirdSetFirst = int(input())
        if thirdSetFirst != -1:
            thirdSet.append(thirdSetFirst)
            while thirdSet[-1] != -1:
                thirdSet.append(int(input()))
            thirdSet.pop(-1)
else:
    thirdSetFirst = int(input())
    if thirdSetFirst != -1:
        thirdSet.append(thirdSetFirst)
        while thirdSet[-1] != -1:
            thirdSet.append(int(input()))
        thirdSet.pop(-1)

combinedList = (firstSet + secondSet + thirdSet)[::-1]

if len(combinedList)%2 == 0:
    for i in range(0, len(combinedList), 2):
        altFirstSet.append(combinedList[i])
        altSecondSet.append(combinedList[i+1])
else:
    for i in range(0, len(combinedList), 2):
        altFirstSet.append(combinedList[i])
        altSecondSet.append(combinedList[i+1])
    altFirstSet.append(combinedList[-1])
    
combinedList = altFirstSet + altSecondSet[::-1]

print(combinedList)

