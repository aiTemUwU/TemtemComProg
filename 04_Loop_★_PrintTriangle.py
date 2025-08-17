h = int(input())
baseStr = "".join("*" for i in range(2*h-1))
triangleStr = [baseStr]

for i in range(1, h-1):
    layer = [" " for i in range(2*h-1)]
    layerStr = ""
    layer[i], layer[-i-1] = "*","*"
    for j in range(0, len(layer)):
        layerStr += layer[j]
    triangleStr.append(layerStr)

triangleStr.append(" "*(h-1) + "*" + " "*(h-1))
triangleStr = triangleStr[::-1]

for i in range(0, h):
    print(triangleStr[i])