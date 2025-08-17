inputParen = ["(", "[", ")", "]"]
outputParen = ["[", "(", "]", ")"]
textList = [str(i) for i in input()]

for i in range(0, len(textList)):
    if textList[i] in inputParen:
        textList[i] = outputParen[inputParen.index(textList[i])]
    else: pass

text = "".join(i for i in textList)
print(text)