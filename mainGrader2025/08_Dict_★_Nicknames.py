firstNameList, nickNameList = [], []
outPut = []

for i in range(0, int(input())):
	firstName, nickName = input().split()
	
	firstNameList.append(firstName)
	nickNameList.append(nickName)

for i in range(0, int(input())):
	firstOrNick = input()

	if firstOrNick not in firstNameList + nickNameList:
		outPut.append("Not found")
	elif firstOrNick in firstNameList:
		outPut.append(nickNameList[firstNameList.index(firstOrNick)])
	elif firstOrNick in nickNameList:
		outPut.append(firstNameList[nickNameList.index(firstOrNick)])
		
for i in range(0, len(outPut)):
	print(outPut[i])