data = input().strip()
allyGroupList = []
enemyPairDict1, enemyPairDict2 = {}, {}


def isEnemy(a, b):
    for rival in enemyPairDict1.keys():
        if a in rival and b in enemyPairDict1.get(rival): return True
    for rival in enemyPairDict2.keys():
        if a in rival and b in enemyPairDict2.get(rival): return True
    
    return False


while data != "End":
    if data.split()[0] == "Ally":
        allyGroupList.append(data.split()[1::])
        

    if data.split()[0] == "Enemy":
        rival1, rival2 = data.split()[1], data.split()[2]
        rivalTuple1, rivalTuple2 = tuple([]), tuple([])

        for group in allyGroupList:
            if rival1 in group: rivalTuple1 = tuple(group)
            if rival2 in group: rivalTuple2 = tuple(group)
        
        if len(rivalTuple1) == 0: rivalTuple1 = tuple([rival1])
        if len(rivalTuple2) == 0: rivalTuple2 = tuple([rival2])

        enemyPairDict1.update({rivalTuple1:rivalTuple2})
        enemyPairDict2.update({rivalTuple2:rivalTuple1})


    if data.split()[0] == "Table":
        isPossible = True
        countryList = data.split()[1::] + [data.split()[1]]

        for i in range(0, len(countryList)-1):
            country1, country2 = countryList[i], countryList[i+1]
            if isEnemy(country1, country2): isPossible = False

        if isPossible: print("Okay")
        else: print("No")

    data = input().strip()

"""
Ally America England Ukraine France
Ally Russia China
Enemy China America
Enemy France Iran
Enemy Iran Iraq
Table America England Iceland France Iran Russia Iraq
Table America England Russia
Table America England Thailand Russia China Iran China Japan
End
"""