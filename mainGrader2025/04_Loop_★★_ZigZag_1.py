xList = []
yList = []
redData = []
blueData = []

N = int(input())

for i in range(0, N):
    pair = input().split()
    xList.append(int(pair[0]))
    yList.append(int(pair[1]))

if N % 2 != 0:
    xList.append(yList[N-1])
    yList.append(xList[N-1])
else: pass

mode = input()

if mode == "Zig-Zag":
    for i in range(0, N, 2):
        redData.append(xList[i])
        redData.append(yList[i+1])
        
        blueData.append(yList[i])
        blueData.append(xList[i+1])
else:
    for i in range(0, N, 2):
        blueData.append(xList[i])
        blueData.append(yList[i+1])
    
        redData.append(yList[i])
        redData.append(xList[i+1])
        
minVal = min(redData)
maxVal = max(blueData)

print(f"{minVal} {maxVal}")