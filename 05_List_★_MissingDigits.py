num = input()
numList = [str(i) for i in range(0, 10)]

for i in range(0, len(num)):
    if num[i] in numList:
        numList.remove(num[i])
    else: pass

if len(numList) != 0:
    displayList = ''.join(i+"," for i in numList)
    displayList = displayList[0:len(displayList)-1]
    print(displayList)
else: print("None")