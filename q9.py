import numpy as np
import math

def is_square(n):
    sqrt = math.sqrt(n)
    return sqrt == n


for a in range(600):
    for b in range(a):
        c_squared = a**2+b**2
        c = np.sqrt(c_squared)
        if a+b+c==1000:
            print(a,b,c,a+b+c,a*b*c)

