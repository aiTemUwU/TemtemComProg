x = input().split()
t, w, c = int(x[0]), int(x[1]), x[2]

if t not in (1, 2, 3):
    p_s = "InvalidTicket"
    total = 0
else:
    if t == 1: tp, fb, ef = 2000, 20, 500
    elif t == 2: tp, fb, ef = 5000, 30, 300
    else: tp, fb, ef = 8000, 40, 100
    
    total = float(tp)
    e = w - fb
    
    if e > 0:
        bu = (e - 1) // 5 + 1
        total += bu * ef

    if len(c) == 8:
        if c[-3:] in ('UOB', 'SCB'):
            total *= 0.9
            p_s = "Discount"
        else: p_s = "NoDiscount"
    else: p_s = "InvalidPromocode"

print(p_s, round(total))