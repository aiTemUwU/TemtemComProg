n = list(input())
preN12 = 0
outPut = ''

for i in range(0, len(n)):
    preN12 += (13-i)*int(n[i])
    
N12 = (11-(preN12 % 11)) % 10

n.append(N12)
n.insert(1, " ")
n.insert(6, " ")
n.insert(12, " ")
n.insert(15, " ")

for i in range(0, len(n)):
    outPut += str(n[i])
    
print(outPut)