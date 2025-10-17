num = [int(i) for i in input().split()]
print(len(set(num)))
if len(set(num)) >= 10: print(sorted(list(set(num)))[0:10])
else: print(sorted(list(set(num))))