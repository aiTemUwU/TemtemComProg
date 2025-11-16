n = int(input())
if n <= 0:
    print(0.0)
else:
    pi_over_4 = 0.0
    for k in range(n):
        pi_over_4 += ((-1)**k) / (2*k + 1)
    ans = 4 * pi_over_4
    print(round(ans, 16))