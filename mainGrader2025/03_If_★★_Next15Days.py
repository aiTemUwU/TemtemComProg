d, m, y = [int(e) for e in input().split()]
y -= 543
n = 31
m30d = [4, 6, 9, 11]

if m in m30d:
    n = 30
else:
    if m == 2:
        n = 28
        if y % 400 == 0:
            n = 29
        if y % 4 == 0 and y % 100 != 0:
            n = 29
d += 15
if d > n:
    d -= n
    m += 1
if m > 12:
    m -= 12
    y += 1
y += 543


print(f"{d}/{m}/{y}")
