firstToNick, nickToFirst = {}, {}

for i in range(0, int(input())):
	firstName, nickName = input().split()

	firstToNick.update({firstName:nickName})
	nickToFirst.update({nickName:firstName})

for i in range(0, int(input())):
	firstOrNick = input()

	if firstOrNick not in firstToNick.keys() and firstOrNick not in nickToFirst.keys():
		print("Not found")
	elif firstOrNick in firstToNick.keys():
		print(firstToNick.get(firstOrNick))
	elif firstOrNick in nickToFirst.keys():
		print(nickToFirst.get(firstOrNick))
