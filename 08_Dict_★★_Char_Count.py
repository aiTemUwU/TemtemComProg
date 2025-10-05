text = input().lower()
alpDict = {}
comparingList = []

for i in range(0, len(text)):
	if text[i] not in alpDict.keys():
		alpDict.update({text[i]:1})
	else:
		alpRep = alpDict.get(text[i])
		alpDict.update({text[i] : alpRep + 1})

for e in alpDict.keys():
	comparingList.append([-alpDict.get(e), e])

comparingList = sorted(comparingList)

for i in range(0, len(comparingList)):
	print(f"{comparingList[i][1]} -> {-comparingList[i][0]}")