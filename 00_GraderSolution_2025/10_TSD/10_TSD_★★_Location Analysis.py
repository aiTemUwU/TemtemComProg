IDtoCity = {}
output, filteredOutput = [], []

def reverse(dict):
    reverseDict = {}
    for e in dict.keys():
        reverseDict.update({dict.get(e):e})
    return reverseDict

for i in range(0, int(input())):
    ID, cities = input().split(": ")
    citiesTuple = tuple(cities.split(", "))

    if ID not in IDtoCity.keys(): IDtoCity.update({ID:citiesTuple})
    else: IDtoCity.update({ID:IDtoCity.get(ID) + citiesTuple})

CitytoID = reverse(IDtoCity)
keyID = input()
keyCities = IDtoCity.get(keyID)

for cities in keyCities:
    for reverseKey in CitytoID.keys():
        if cities in reverseKey: output.append(CitytoID.get(reverseKey))
        else: pass

for e in output:
    if e == keyID: pass
    else:
        if e in filteredOutput: pass
        else: filteredOutput.append(e)

if len(filteredOutput) == 0: print("Not Found")
else:
    for e in IDtoCity.keys():
        if e in filteredOutput: print(e)
        else: pass
