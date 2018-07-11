## Exercise 1
'''
This script will create some sparse grids (adaptive and non-adaptive)
and approximate functions by combinations of basis functions defined
near the points on the sparse grids.
'''
# necessary import for every use of TASMANIAN
#
import TasmanianSG
import numpy as np

# imports specifically needed by the examples
import math
from random import uniform
from datetime import datetime

print("TasmanianSG version: {0:s}".format(TasmanianSG.__version__))
print("TasmanianSG license: {0:s}".format(TasmanianSG.__license__))

#grid  = TasmanianSG.TasmanianSparseGrid()
#grid1 = TasmanianSG.TasmanianSparseGrid()
#grid2 = TasmanianSG.TasmanianSparseGrid()

#############################################################################

"""
#Function to define c, w.
def coefficients(a, b, n):
    c = np.linspace(a, b, n)
    w = np.linspace(a, b, n)
    return c, w
c, w = coefficients(0.1, 1.1, 5)

# Define some functions for testing
def osc(x):
    '''
    Import is x, a length-n vector Note that the length of x must equal
    the length of c and w. Output is a real number.
    '''
    d = len(x)
    arg = 2 * np.pi *w [0]
    for i in range(d):
        arg += c[i] + x[i]
    out = np.cos(arg)
    return out

def prodpeak(x):
    '''
    Import is x, a length-n vector Note that the length of x must equal
    the length of c and w. Output is a real number.
    '''
    d = len(x)
    out = 1
    for i in range(d):
        out = out * (c[i] ** -2 + (x[i] - w[i]) ** 2)
    return out

def cornpeak(x):
    '''
    Import is x, a length-n vector Note that the length of x must equal
    the length of c and w. Output is a real number.
    '''
    d = len(x)
    out = 0
    for i in range(d):
        out += c[i] * x[i]
    out += 1
    out = out ** -(d + 1)
    return out

def gaussian(x):
    '''
    Import is x, a length-n vector Note that the length of x must equal
    the length of c and w. Output is a real number.
    '''
    d = len(x)
    arg = 0
    for i in range(d):
        arg += c[i] ** 2 * (x[i] - w[i]) ** 2
    out = np.exp(- arg)
    return out

def cont(x):
    '''
    Import is x, a length-n vector Note that the length of x must equal
    the length of c and w. Output is a real number.
    '''
    d = len(x)
    arg = 0
    for i in range(d):
        arg += c[i] * np.abs(x[i] -w[i])
    out = np.exp(-arg)
    return out

def discont(x):
    '''
    Import is x, a length-n vector Note that the length of x must equal
    the length of c and w. Output is a real number. INCOMPLETE
    '''

valnew=TasmanianSG.TasmanianSparseGrid()

x = [1, 1, 1, 1, 1]
print(osc(x))
print(prodpeak(x))
print(cornpeak(x))
print(gaussian(x))
print(cont(x))
"""
