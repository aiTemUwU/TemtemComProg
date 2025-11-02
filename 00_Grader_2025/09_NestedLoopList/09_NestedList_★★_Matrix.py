def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c, A):
    row, col = len(A), len(A[0])
    for i in range(0, row):
        for j in range(0, col):
            A[i][j] *= c
    return A

def mult(A, B):
    result, subResult = [], []
    Rrc = 0
    rowA, colA = len(A), len(A[0])
    rowB, colB = len(B), len(B[0])

    for i in range(0, rowA):
        for j in range(0, colB):
            for k in range(0, colA):
                Rrc += (A[i][k] * B[k][j])
            subResult.append(Rrc)
            Rrc = 0
        result.append(subResult)
        subResult = []

    return result

exec(input().strip())
