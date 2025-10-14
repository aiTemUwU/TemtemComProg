num = input()
roundedNum = ""
abre = ""

if len(num) > 9:
    roundedNum = int(num)/10**9
    abre = "B"
elif len(num) > 6:
    roundedNum = int(num)/10**6
    abre = "M"
elif len(num) > 3:
    roundedNum = int(num)/10**3
    abre = "K"
else: roundedNum = float(num)

if len(num) in [4, 7, 10]:
    roundedNum = round(roundedNum, 1)
else:
    roundedNum = round(roundedNum)

print(f"{roundedNum}{abre}")