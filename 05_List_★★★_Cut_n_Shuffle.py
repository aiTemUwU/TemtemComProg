cards = input().split()
actions = input().split()
actionsList = []
output = ""

def cut(cards):
    firstHalf = cards[0: int(len(cards)/2)]
    secondHalf = cards[int(len(cards)/2): len(cards)]
    
    return secondHalf + firstHalf


def shuffle(cards):
    shuffledCards = []
    
    firstHalf = cards[0: int(len(cards)/2)]
    secondHalf = cards[int(len(cards)/2): len(cards)]
    
    for i in range(0, int(len(cards)/2)):
        shuffledCards.append(firstHalf[i])
        shuffledCards.append(secondHalf[i])
    
    return shuffledCards


for i in range(0, len(actions)):
    if len(actions[i]) == 1:
        if "C" or "S" in actions[i]:
            if actions[i] not in ["C", "S"]:
                if "C" in actions[i]: actionsList.append("C")
                if "S" in actions[i]: actionsList.append("S")
            else: actionsList.append(actions[i])
        else: pass
    else:
        for j in range(0, len(actions[i])):
            if actions[i][j] == "C": actionsList.append("C")
            if actions[i][j] == "S": actionsList.append("S")
            else: pass


for i in range(0, len(actionsList)):
    if actionsList[i] == "C": cards = cut(cards)
    else: cards = shuffle(cards)
    
for i in range(0, len(cards)):
    output += (cards[i] + " ")

print(output[0: len(output)-1])