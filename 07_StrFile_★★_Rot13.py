lowerAlp = "abcdefghijklmnopqrstuvwxyz"
upperAlp = lowerAlp.upper()

outPut = ""
text = input()

while text != "end":
	for i in range(0, len(text)):
		if text[i] in lowerAlp:
			pos = lowerAlp.index(text[i]) + 13
			if pos > 24: pos -= 26
			else: pass
			
			outPut += lowerAlp[pos]
		elif text[i] in upperAlp:
			pos = upperAlp.index(text[i]) + 13
			if pos > 24: pos -= 26
			else: pass
			
			outPut += upperAlp[pos]
		else:
			outPut += text[i]

	outPut += "\n"
	text = input()

print(outPut)