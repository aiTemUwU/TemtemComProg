def row_number(t, e):
    for row in t:
        if e in row:
            return t.index(row)

def flatten(t):
    output = []
    row, col = len(t), len(t[0])

    for i in range(0, row):
        for j in range(0, col):
            if t[i][j] != 0:
                output.append(t[i][j])
            else: pass

    return output

def inversions(x):
    iteratingList, inversions = [], 0

    for i in range(0, len(x)):
        for j in range(i+1, len(x)):
            iteratingList.append((x[i], x[j]))

    for e in iteratingList:
        if e[0] > e[1]: inversions += 1
        else: pass

    return inversions

def isEven(n):
    if n % 2 == 0: return True
    return False

def solvable(t):
    if not isEven(len(t)):
        if isEven(inversions(flatten(t))): return True
        else: pass
    elif isEven(len(t)):
        if not isEven(inversions(flatten(t))):
            if isEven(row_number(t, 0)): return True
        elif isEven(inversions(flatten(t))):
            if not isEven(row_number(t, 0)): return True
        else: pass
    return False

exec(input().strip())
