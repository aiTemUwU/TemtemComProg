file1, file2= input().split()
text = input()
posList, negList = [], []



#reading and storing file ----------
f1 = open(file1, "r")
f2 = open(file2, "r")

for line in f1: posList.append(line.strip())
for line in f2: negList.append(line.strip())

f1.close()
f2.close()



#filtering out punctuation ---------
filteredText, result = "", ""

for e in text:
	if e.isalpha() or e == " ": filteredText += e.lower()
	else: pass

filteredTextList = filteredText.split()



#checking for matching word ---------
posCount, negCount, neuCount = 0, 0, 0

for e in filteredTextList:
	if e in posList: posCount += 1
	if e in negList: negCount += 1
	if e not in posList + negList: neuCount += 1



#output ----------
wordCount = len(filteredTextList)
totalCount = posCount - negCount

if totalCount > 0: result = "Positive"
if totalCount < 0: result = "Negative"
if totalCount == 0: result = "Neutral"

print(f"{wordCount} {posCount} {negCount} {neuCount}")
print(f"{totalCount} {result}")



'''
neg.txt-----

2-faced
2-faces
abnormal
abolish
abominable
abominably
abominate
abomination
abort
aborted
aborts
abrade
abrasive
difficult
hate
badly
arrogance
greedy
bad

'''

'''
pos.txt-----
a+
abound
abounds
abundance
abundant
accessable
accessible
acclaim
acclaimed
acclamation
accolade
accolades
accommodative
super
easy
cute
lovely
handsome
love

'''
