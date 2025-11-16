data, sortingList = {}, []

for i in range(0, int(input())):
	for j in range(0, int(input())):
		name, point = input().split()
		
		if name in data.keys(): data.update({name:data.get(name)+int(point)})
		else: data.update({name:int(point)})

#sorting part----------
for e in data.keys(): sortingList.append([-data.get(e), e])
sortingList = sorted(sortingList)

for e in sortingList:
	print(f"{e[1]} {-e[0]}")