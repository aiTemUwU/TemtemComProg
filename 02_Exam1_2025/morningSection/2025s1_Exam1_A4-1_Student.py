n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    total_sum = 0
    for _ in range(n):
        total_sum += a
        a, b = b, a + b
    print(total_sum)