data, year = [input() for i in range(0, 2)]
output = []
currentCode = ""

for i in range(0, len(data)):
	if i == len(data)-9: break
	
	elif data[i] + data[i+1] == year:
		for j in range(i, i+10):
			if data[j] < "A":
				currentCode += data[j]
			else:
				currentCode = ""
				break
		if currentCode[-2::] == "21":
			if currentCode != "":
				output.append(currentCode)
				currentCode = ""
		else: currentCode = ""

if len(output) == 0: print("Not found")
else:
	for i in range(0, len(output)):
		print(output[i])
