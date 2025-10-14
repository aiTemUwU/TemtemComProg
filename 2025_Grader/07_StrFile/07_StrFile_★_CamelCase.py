text = input()
newText = ""
outPut = ""

for i in range(0, len(text)):
	if text[i] == " ":
		newText += text[i]
	elif text[i].isdigit():
		newText += text[i]
	elif text[i].isalpha():
		newText += text[i].lower()
	else:
		newText += " "

newText = newText.split()
for i in range(0, len(newText)):
	if text[i].isalpha:
		newText[i] = newText[i][0].upper() + newText[i][1::]
	else: pass

	outPut += newText[i]

outPut = outPut[0].lower() + outPut[1::]
print(outPut)
