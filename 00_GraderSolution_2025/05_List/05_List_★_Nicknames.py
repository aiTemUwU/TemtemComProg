fullName = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nickName = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]
outputName = []

N = int(input())
for i in range(0, N):
    inputName = input()
    if inputName in fullName:
        outputName.append(nickName[fullName.index(inputName)])
    elif inputName in nickName:
        outputName.append(fullName[nickName.index(inputName)])
    else:
        outputName.append("Not found")

for i in range(0, N):
    print(outputName[i])