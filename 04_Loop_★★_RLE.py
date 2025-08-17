text = input() + "$"
alp = []
letter = ""
rep = 0
output = ""

for i in range(0, len(text)):
    if rep == 0:
        letter = text[i]
        rep += 1
    elif text[i] == text[i-1]:
        rep += 1
    else:
        alp.append([letter, rep])
        rep, letter = 1, text[i]
        
for i in range(0, len(alp)):
    output += f"{alp[i][0]} {alp[i][1]} "

print(output)