salesInput = input().split()
salesList = []

for i in range(0, len(salesInput)):
    salesList.append(int(salesInput[i]))
    
print(sum(salesList))