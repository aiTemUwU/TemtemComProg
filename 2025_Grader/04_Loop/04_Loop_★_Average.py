numList = []
num1 = input()

while num1 != "q":
    numList.append(float(num1))
    num1 = input()

if numList == []:
    print("No Data")
else:
    avg = round(sum(numList)/len(numList), 2)
    print(avg)