num = [float(i) for i in input().split()]
peakCounter = 0

for i in range(1, len(num)-1):
    if num[i] > num[i-1] and num[i] > num[i+1]:
        peakCounter += 1

print(peakCounter)
