import numpy as np

def get_column_from_bottom_to_top(A, c):
    return A[:, c][::-1]

def get_odd_rows(A):
    return A[1::2]

def get_even_column_last_row(A):
    return A[-1, ::2]

def get_diagonal1(A):
    return np.sum(A * np.identity(len(A), dtype = int), axis = 0)

def get_diagonal2(A):
    reverseIden = np.identity(len(A), dtype = int)[::-1]
    return np.sum(A * reverseIden, axis = 0)

exec(input().strip())