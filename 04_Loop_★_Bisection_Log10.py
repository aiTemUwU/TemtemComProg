a = float(input())
L, U = 0, a
x = (L+U)/2

while abs(10**x-a) > 1e-10*a:
    if 10**x > a:
        U = x
    else: L = x
    x = (L+U)/2

print(round(x, 6))