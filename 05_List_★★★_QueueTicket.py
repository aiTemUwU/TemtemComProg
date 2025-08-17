qNum = 0
nextCounter = 0
qData = []
ready2order = []
avgdt = []

for i in range(0, int(input())):
    command = input().split()
    if command[0] == "reset":
        qNum = int(command[1])
    if command[0] == "new":
        qData.append([qNum, command[1]])
        print(f"ticket {qNum}")
        qNum += 1
    if command[0] == "next":
        print(f"call {qData[nextCounter][0]}")
        ready2order = qData[nextCounter]
        nextCounter += 1
    if command[0] == "order":
        dt = int(command[1]) - int(ready2order[1])
        avgdt.append(int(dt))
        print(f"qtime {ready2order[0]} {dt}")
    if command[0] == "avg_qtime":
        avg = sum(avgdt)/len(avgdt)
        print(f"avg_qtime {round(avg, 6)}")
