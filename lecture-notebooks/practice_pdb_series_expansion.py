'''
    
    Note: this is a series expansion, but NOT a Taylor Series!
    The usual Taylor series for log(1+x) has a converge range of -1<x<=1
    This is based on ln(x) = sum( (1/n) ((x-1)/x)^n ) -- replacing x by x + 1, 
    we get the formula below.
    
    The advantage is now the convergence radius is x > -1
    
    Two caveats: 
    
    1. for x < -1, the series approximation gives a *bogus* answer!!!!
    2. for large x (say x = 100, n needs to be > 100 to get a precise value)
    
    For this to be a well-written function, these two issues have be dealt with
    
'''


import pdb
from math import log  #you would guess math module would have log...yes!
from math import log1p  #more accurate for small x.

def L(x, n):
    pdb.set_trace()
    for i in range(1, n + 1):
        approx += (1/(i+1))*(x/(1+x))**(i+1)
    return approx
    return approx


x = 2
approx = 0
y = L(x, 100)
print('Series Expansion Approximation:', y)

exact_val = log(1+x)
print('exact_val', exact_val)
print('log1p output', log1p(x))
