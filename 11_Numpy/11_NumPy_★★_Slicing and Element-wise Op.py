import numpy as np

def sum_2_rows(M):
    return M[::2] + M[1::2]

def sum_left_right(M):
    left = M[:, 0:int(len(M[0])/2)]
    right = M[:, int(len(M[0])/2):]

    return left + right

def sum_upper_lower(M):
    upper = M[:int(len(M)/2)]
    lower = M[int(len(M)/2):]

    return upper + lower

def sum_4_quadrants(M):
    Q2 = M[:int(len(M)/2), :int(len(M[0])/2)]
    Q1 = M[:int(len(M)/2), int(len(M[0])/2):]
    Q3 = M[int(len(M)/2):, :int(len(M[0])/2)]
    Q4 = M[int(len(M)/2):, int(len(M[0])/2):]

    return Q1 + Q2 + Q3 + Q4

def sum_4_cells(M):
    m00 = M[::2, ::2]
    m01 = M[::2, 1::2]
    m10 = M[1::2, ::2]
    m11 = M[1::2, 1::2]

    return m00 + m01 + m10 + m11

def count_leap_years(years):
    years = years - 543

    years1 = years[years%400 == 0]
    years2 = years[(years%4 ==0) & (years%100 !=0) & (years%400!=0)]

    return len(np.concatenate((years1, years2)))

exec(input().strip())