a = float(input())
L = 0
U = 0
loopA = a

while loopA != 0:
    U += 1
    loopA //= 10

x = (U+L)/2

while not abs(a-10**x) <= 10**(-10)*max(a, 10**x):
    if 10**x < a: L = x
    else: U = x
    x = (U+L)/2
    
print(round(x, 6))