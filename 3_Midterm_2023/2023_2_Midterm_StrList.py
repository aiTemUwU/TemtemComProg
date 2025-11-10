menuDict = {}
totalPrice = 0

n, m = [int(e) for e in input().split()]

for i in range(0, n):
	data = input()
	menuName, price = "", ""
	
	for i in range(0, len(data)):
		if data[i].isalpha() or data[i] == " ": menuName += data[i]
		else:
			price = data[i::]
			break 
	
	menuDict.update({menuName.strip():float(price)})

for i in range(0, m):
	data = input()
	menuName, amount = "", ""
	
	for i in range(0, len(data)):
		if data[i].isalpha() or data[i] == " ": menuName += data[i]
		else:
			amount = int(data[i::])
			totalPrice += menuDict.get(menuName.strip()) * amount
			break

print(totalPrice)