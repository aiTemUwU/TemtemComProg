genre2time = {}
sortingList = []

def totTimeFormat(totTime):
    min = totTime // 60
    sec = totTime - (min*60)

    if len(str(sec)) == 1:
        sec = "0" + str(sec)
    else: pass

    return f"{min}:{sec}"

for i in range(0, int(input())):
    songName, singerName, genre, time = input().split(", ")

    min, sec = time.split(":")
    totTime = (int(min)*60) + int(sec)

    if genre not in genre2time.keys():
        genre2time.update({genre:totTime})
    else: genre2time.update({genre:genre2time.get(genre)+totTime})

for genre in genre2time.keys():
    sortingList.append([genre2time.get(genre), genre])

sortingList = sorted(sortingList)[::-1]

if len(sortingList) <= 3:
    for i in range(0, len(sortingList)):
        print(f"{sortingList[i][1]} --> {totTimeFormat(sortingList[i][0])}")
else:
    for i in range(0, 3):
        print(f"{sortingList[i][1]} --> {totTimeFormat(sortingList[i][0])}")
