Alp = "ABCDEFGHIJKLMNOPQRSTTUVWXYZ"
code = input()

A = "".join(code[(7*i)+3] for i in range(0, 5))
B = "".join(code[(5*i)+7] for i in range(0, 5))
C = 10000+int(A)+int(B)
D = str(C)[len(str(C))-2:len(str(C))-5:-1][::-1]
E = int(str(sum([int(D[i]) for i in range(0, len(D))]))[-1::])+1
F = Alp[E-1]
G = f"{D}{F}"

print(G)