import numpy as np

def mult_table(nrows, ncols):
    nRowMat = np.arange(1, nrows+1).reshape(nrows, 1)
    nColMat = np.arange(1, ncols+1).reshape(1, ncols)

    return np.multiply(nRowMat, nColMat)


exec(input().strip())