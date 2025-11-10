text1, text2 = [input().lower() for i in range(0, 2)]
alp1, alp2 = [], []
numAlp1, numAlp2 = [], []
alpSum1, alpSum2 = [], []

for i in range(0, len(text1)):
	if text1[i] not in alp1:
		alp1.append(text1[i])
		numAlp1.append(1)
	elif text1[i] == " ": pass
	else:
		numAlp1[alp1.index(text1[i])] += 1

for i in range(0, len(text2)):
	if text2[i] not in alp2:
		alp2.append(text2[i])
		numAlp2.append(1)
	elif text2[i] == " ": pass
	else:
		numAlp2[alp2.index(text2[i])] += 1

for i in range(0, len(alp1)):
	alpSum1.append([alp1[i], numAlp1[i]])

for i in range(0, len(alp2)):
	alpSum2.append([alp2[i], numAlp2[i]])

alpSum1 = sorted(alpSum1)
alpSum2 = sorted(alpSum2)

if alpSum1 == alpSum2:
	print("YES")
else:
	print("NO")
