s = input()

if len(s) != 12 or s[3] != '-' or s[7] != '-':
    print("Error1")
else:
    n = s.replace('-', '')
    if not n.isdigit() or len(n) != 10:
        print("Error2")
    else:
        score = (int(n[0]) * 1 + int(n[2]) * 3 + int(n[4]) * 5 + int(n[6]) * 7 + int(n[8]) * 9) % 100
        
        if score <= 19: p = "Calm"
        elif score <= 39: p = "Creative"
        elif score <= 59: p = "Energetic"
        elif score <= 79: p = "Practical"
        else: p = "Lucky"
            
        print(f"{n}={p}")