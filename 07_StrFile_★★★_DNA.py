pairs1 = ["A", "T", "C", "G"]
pairs2 = ["T", "A", "G", "C"]

def isValid(data):
	for e in data:
		if e not in pairs1:
			return False 
	return True

def reverse(data):
	output = ""
	for i in range(0, len(data)):
		output += pairs2[pairs1.index(data[i])]
	output = output[::-1]
	
	return output

def freq(data):
	freq = [0, 0, 0, 0]
	for e in data:
		freq[pairs1.index(e)] += 1
	return freq

def display(data):
	checkFor = input().strip()
	pairs = 0
	
	for i in range(1, len(data)):
		checking = data[i-1] + data[i]
		if checking == checkFor:
			pairs += 1
		else: pass
	
	return pairs

def main():
	data = input().strip().upper()
	operator = input().strip()
	if not isValid(data):
		print("Invalid DNA")
	else:
		if operator == "R":
			print(reverse(data))
		if operator == "F":
			A, T, C, G = freq(data)
			print(f"A={A}, T={T}, G={G}, C={C}")
		if operator == "D":
			print(display(data))
	return

if __name__ == "__main__":
	main()
	