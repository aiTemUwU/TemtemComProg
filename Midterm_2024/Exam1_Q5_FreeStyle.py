transaction = input().split(",")
bookID = []
memberID = []
borrowing = []

borrowedNum = 0
returnedNum = 0
notReturnedNum = 0
returnedWithFine = 0
fine = 0

for i in range(0, len(transaction)):
	if transaction[i][0:3] not in bookID:
		bookID.append(transaction[i][0:3])
		memberID.append(transaction[i][3:6])
		borrowing.append(int(transaction[i][7::]))
		borrowedNum += 1
	else:
		if transaction[i][7::] == "**":
			notReturnedNum += 1
		elif int(transaction[i][7::]) > borrowing[bookID.index(transaction[i][0:3])]:
			fine += (borrowing[bookID.index(transaction[i][0:3])] - int(transaction[i][7::]))*(-2)
			returnedWithFine += 1
			returnedNum += 1
		else:
			returnedNum += 1

print(f"{borrowedNum}\n{returnedNum}\n{notReturnedNum}\n{returnedWithFine}\n{fine}")