n = int(input())
process = [n]
processStr = ""

while n != 1:
    if n%2 == 0: n /= 2
    else: n = 3*n+1
    process.append(int(n))

if len(process) > 15:
    process = process[len(process)-15:len(process)]
else: pass

processStr += (f"{process[0]}")

for i in range(1, len(process)):
    processStr += (f"->{process[i]}")

print(processStr)