text = input().split()
currentOutput = ""
output = ""

for i in range(0, len(text)):
	text[i] = text[i].lower()
	text[i] = text[i][::-1]
	currentOutput = text[i][0].upper() + text[i][1::]
	
	output += f"{currentOutput} "
	
print(output.strip())