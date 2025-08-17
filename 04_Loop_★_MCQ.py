correctAns, stuAns = input().replace(" ", ""), input().replace(" ", "")
score = 0

if len(correctAns) == len(stuAns):
    for i in range(0, len(correctAns)):
        if correctAns[i] == stuAns[i]:
            score += 1
        else: pass
    print(score)
else: print("Incomplete answer")
