info = input()
user = []
grade = []
sortedUser = []
gradeRank = ["F", "D", "D+", "C", "C+", "B", "B+", "A"]

while info != "q":
    info = info.split()
    user.append(info[0])
    grade.append(info[1])
    info = input()

upUser = input().split()

for i in range(0, len(user)):
    if user[i] in upUser:
        grade[i] = gradeRank[gradeRank.index(grade[i])+1]
    else: pass

sortedUser = sorted(user)

for i in range(0, len(sortedUser)):
    print(f"{sortedUser[i]} {grade[user.index(sortedUser[i])]}")
