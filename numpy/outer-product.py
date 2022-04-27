
import numpy as np

def mult_table(nrows,ncols):
    a1 = np.arange(1,nrows+1)     #สร้างarray 
    a2 = np.arange(1,ncols+1).reshape((nrows,1))
    return a1*a2

exec(input().strip())