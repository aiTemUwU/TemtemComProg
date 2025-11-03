def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def is_coprime(a, b, c):
    if gcd(a, b) == 1 or gcd(a, c) == 1 or gcd(b, c) == 1: return True
    else: return False

def primitive_Pythagorean_triples(max_len):
    NM, triples = [], []

    for i in range(1, max_len):
        for j in range(i+1, max_len+1):
            NM.append((i, j))

    for e in NM:
        n, m = e[0], e[1]
        c = m**2 + n**2

        if c < max_len:
            a = m**2 - n**2
            b = 2*m*n
            subTriple = [a, b, c]
            subTriple = sorted(subTriple)
            if is_coprime(a, b, c): triples.append(subTriple)
            else: pass
        else: pass

    triples = sorted(triples, key = lambda item: (item[2], item[0]))
    return triples

exec(input().strip())
