text = input().lower()
alpDict = {}
comparingList = []
filteredText = ""

for i in range(0, len(text)):
	if text[i].isalpha():
		filteredText += text[i]
	else: pass

for i in range(0, len(filteredText)):
	if filteredText[i] not in alpDict.keys():
		alpDict.update({filteredText[i]:1})
	else:
		alpRep = alpDict.get(filteredText[i])
		alpDict.update({filteredText[i] : alpRep + 1})

for e in alpDict.keys():
	comparingList.append([-alpDict.get(e), e])

comparingList = sorted(comparingList)

for i in range(0, len(comparingList)):
	print(f"{comparingList[i][1]} -> {-comparingList[i][0]}")
