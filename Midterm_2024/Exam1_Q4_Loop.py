text = input().split()
freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, len(text)):
	freq[int(text[i])] += 1

maxFreq = max(freq)
maxVal = freq.index(maxFreq)
freq.remove(maxFreq)

if maxFreq in freq:
	print("-1")
else:
	if maxFreq >= len(text)/2:
		print(maxVal)
	else:
		print("-1")