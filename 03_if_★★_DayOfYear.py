d, m, y = [int(input()) for i in range(0, 3)]
dayInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayOfYear = 0

y -= 543
if y % 400 == 0:
    dayInMonths[1] = 29
elif y % 4 == 0 and y % 100 != 0:
    dayInMonths[1] = 29
else: pass

for i in range(0, m-1):
    dayOfYear += dayInMonths[i]
dayOfYear += d

print(dayOfYear)