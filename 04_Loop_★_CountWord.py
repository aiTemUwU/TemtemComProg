finding, sentence = input(), [i.strip('"(),.').strip("'") for i in input().split()]
counter = 0

for i in range(0, len(sentence)):
    if sentence[i] == finding:
        counter += 1
    else: pass
    
print(counter)