u = input().strip("[]").split(", ")
v = input().strip("[]").split(", ")

for i in range(0, len(u)):
    u[i] = float(u[i])
    v[i] = float(v[i])
    
r = f"[{u[0] + v[0]}, {u[1] + v[1]}, {u[2] + v[2]}]"

print(f"{u} + {v} = {r}")