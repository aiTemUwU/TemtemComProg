import math

r = float(input())
ans = (4 * r**3 / 3) * (math.pi - 2 / math.sqrt(3))
print(round(ans, 2))