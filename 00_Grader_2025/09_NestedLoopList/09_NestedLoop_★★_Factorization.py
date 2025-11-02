def factor(N):
    factorDict, k = {}, 2
    factorList = []

    while k <= N:
        if N % k == 0:
            if k not in factorDict.keys():
                factorDict.update({k:1})
            else: factorDict.update({k:factorDict.get(k)+1})
            N /= k
        else: k += 1

    for e in factorDict.keys():
        factorList.append([e, factorDict.get(e)])

    return factorList

exec(input().strip())
