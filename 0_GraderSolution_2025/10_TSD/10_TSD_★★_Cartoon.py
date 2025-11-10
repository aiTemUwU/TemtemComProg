type2NameDict = {}

data = input()

while data != "q":
    name, typeName = data.split(", ")

    if typeName not in type2NameDict.keys():
        type2NameDict.update({typeName:[name]})
    else: type2NameDict.update({typeName:type2NameDict.get(typeName) + [name]})

    data = input()

for typeName in type2NameDict.keys():
    nameStr = ""
    for name in type2NameDict.get(typeName):
        nameStr += f"{name}, "

    print(f"{typeName}: {nameStr[:-2]}")
