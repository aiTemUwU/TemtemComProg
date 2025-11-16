s = input()

if len(s) != 13 or s[0] != '(' or s[4] != ')' or s[8] != '-':
    print("Error1")
else:
    n = s[1:4] + s[5:8] + s[9:]
    if not n.isdigit() or len(n) != 10:
        print("Error2")
    else:
        score = (int(n[1]) * 2 + int(n[3]) * 4 + int(n[5]) * 6 + int(n[7]) * 8 + int(n[9]) * 10) % 100
        
        if score <= 19: p = "Cat"
        elif score <= 39: p = "Dog"
        elif score <= 59: p = "Bird"
        elif score <= 79: p = "Rabbit"
        else: p = "Fish"
            
        print(f"{n}={p}")