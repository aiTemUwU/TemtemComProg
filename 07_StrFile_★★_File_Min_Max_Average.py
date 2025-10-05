fileName, year = input().split()
year = year[2::]
code, score = [], []
fitScore = []

data = open(fileName, "r")

if data != "":
    for line in data:
        code.append(line.split()[0])
        score.append(line.split()[1])
    data.close()

    for i in range(0, len(code)):
        if code[i][0:2] == year:
            fitScore.append(float(score[i]))

    if fitScore != []:
        minScore = min(fitScore)
        maxScore = max(fitScore)
        avgScore = sum(fitScore)/len(fitScore)

        print(f"{minScore} {maxScore} {avgScore}")
    else:
        print("No data")

else:
    data.close()
    print("No data")

'''
contents in data.txt:

6230012121 90.0
6130351221 80.0
6231027921 80.0
5830548121 65.5
6031087221 79.9
6230550321 70.0
6230432721 60.0
6230215221 50.0
6130518321 70.0

'''