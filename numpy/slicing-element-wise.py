import numpy as np

def sum_2_rows(M):
    return M[0::2,:] + M[1::2,:]

def sum_left_right(M):
    n = M.shape[1]   #จำนวน culum
    return M[:,: n//2] + M[:,n//2:]

def sum_upper_lower(M):
    n = M.shape[0]   #จำนวน row
    return M[:n//2,: ] + M[ n//2:,:]

def sum_4_quadrants(M):
    return sum_left_right(sum_upper_lower(M))

def sum_4_cells(M):
    return M[::2,::2] + M[::2,1::2] + \
           M[1::2,::2] + M[1::2,1::2]

def count_leap_years(years):
    y = years -543
    return np.sum((y%400 == 0 ) | ((y%4 == 0) & (y%100 != 0)))
    


exec(input().strip())