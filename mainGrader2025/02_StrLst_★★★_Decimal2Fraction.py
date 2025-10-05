import math

whole, nonRep, rep = input().split(",")

A = int(whole + nonRep + rep)-int(whole + nonRep)
B = int("".join("9" for i in range(len(rep)))+"".join("0" for i in range(len(nonRep))))
gcd = math.gcd(A, B)

print(f"{int(A//gcd)} / {int(B//gcd)}")
