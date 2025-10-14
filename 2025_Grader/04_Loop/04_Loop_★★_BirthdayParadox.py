p = float(input())
k = 1
t = 1

def loop(t, k, p):
    t = (t*(365-(k-1)))/365
    if 1-t >= p:
        print(k)
    else:
        k += 1
        loop(t, k, p)
        
loop(t, k, p)