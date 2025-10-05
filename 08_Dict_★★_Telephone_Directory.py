name2num, num2name = {}, {}

for i in range(0, int(input())):
	firstName, lastName, num = input().split()
	
	name2num.update({firstName + " " + lastName:num})
	num2name.update({num:firstName + " " + lastName})

for i in range(0, int(input())):
	numOrName = input()

	if numOrName in num2name.keys():
		print(f"{numOrName} --> {num2name.get(numOrName)}")
	elif numOrName in name2num.keys():
		print(f"{numOrName} --> {name2num.get(numOrName)}")
	else:
		print(f"{numOrName} --> Not found")