teamToCountry = {}
isIllegal = False

for i in range(0, int(input())):
    team, country = input().split()
    teamToCountry.update({team:country})

data = input()
while data != "q":
    teamCountrySet = set([])
    
    group = data.split()
    for team in group:
        if team not in teamToCountry.keys():
            isIllegal = True
            break
        else:
            teamCountrySet.add(teamToCountry.get(team))
            
    
    if isIllegal:
        print("Not OK")
        isIllegal = False
    else:
        if len(teamCountrySet) == len(group): print("OK")
        else: print("Not OK")
    
    data = input()
    
"""
10
Liverpool England
ManCity England
Bayern Germany
Dortmund Germany
Barcelona Spain
Milan Italy
PSG France
Ajax Holland
Real Spain
Celtic Scotland
Liverpool Dortmund Milan Ajax
Liverpool Barcelona PSG Real
ManCity Milan PSG Ajax Celtic
ManCity Ajax SamyamFC Real Bayern
q
"""