exec(input().strip()[4:])
print("spj")
n = int(input())
firstNum = int(input())
secondNum = int(input())

biggestNum = 0
biggestNum2 = 0

if firstNum > secondNum:
	biggestNum = firstNum
	biggestNum2 = secondNum
if secondNum > firstNum:
	biggestNum = secondNum
	biggestNum2 = firstNum
else:
	biggestNum, biggestNum2 = firstNum, secondNum
	
for i in range(0, n-2):
	newNum = int(input())
	if newNum > biggestNum:
		biggestNum2 = biggestNum
		biggestNum = newNum
	elif newNum == biggestNum:
		biggestNum2 = newNum
	elif newNum > biggestNum2:
		biggestNum2 = newNum
		
print(f"{biggestNum} {biggestNum2}")