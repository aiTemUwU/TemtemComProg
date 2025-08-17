import math

bd, bm, by, d, m, y = [int(i) for i in input().split()]


def dayOfYear(d, m, y):
    
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
    
    dayLeft = sum(dayInMonths) - dayOfYear
    
    return [dayOfYear, dayLeft]


redPeriod = dayOfYear(bd, bm, by)[1] + 1
bluePeriod = dayOfYear(d, m, y)[0] - 1
blackPeriod = (365*(y-by-1)) if y - by != 1 else 0

t = redPeriod + bluePeriod + blackPeriod

phy = "{:.2f}".format(math.sin((2*math.pi*t)/23))
emo = "{:.2f}".format(math.sin((2*math.pi*t)/28))
intel = "{:.2f}".format(math.sin((2*math.pi*t)/33))

print(f"{t} {phy} {emo} {intel}")
