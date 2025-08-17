M = input()
N = int(input())

if len(M) < N:
    while len(M) < N:
        M = "0" + M

print(M)