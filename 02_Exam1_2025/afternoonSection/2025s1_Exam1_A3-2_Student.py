x = input().split()
A, B, C = int(x[0]), float(x[1]), int(x[2])

valid = True
if A == 10: bp, fd, fcm = 499, 40, 250
elif A == 15: bp, fd, fcm = 699, 60, 300
elif A == 30: bp, fd, fcm = 1199, 100, 350
else: valid = False

if not valid: print("InvalidPlan")
else:
    total = float(bp)
    
    if B > fd:
        if A == 10: total += (B - fd) * 50
        elif A == 15: total += (B - fd) * 75
        else: total += (B - fd) * 100
            
    fcs = fcm * 60
    
    if C > fcs:
        ecs = C - fcs
        if A == 10: total += ecs * 0.5
        elif A == 15: total += (ecs / 60) * 1
        else: total += (ecs / 60) * 1.5
            
    print(round(total))