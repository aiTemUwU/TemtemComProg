finding, sentence = input(), input()
remove = ["(", ")", ",", ".", '"', "'"]
newSentence = ""

for i in range(0, len(sentence)):
    if sentence[i] not in remove:
        newSentence += sentence[i]
    else:
        newSentence += " "

newSentence = newSentence.split()
counter = 0

for i in range(0, len(newSentence)):
    if newSentence[i] == finding:
        counter += 1
    else: pass

print(counter)
