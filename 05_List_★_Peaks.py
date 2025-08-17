Num = [float(i) for i in input().split()]
peakList = []

for i in range(1, len(Num)-1):
    peak = max(Num[i-1], Num[i], Num[i+1])
    if peak == Num[i+1]: pass
    else:
        peakList.append(peak)
        Num[Num.index(peak)] = Num[i+1]
    
print(len(peakList))