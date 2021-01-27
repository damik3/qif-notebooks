import numpy as np
from qif import *

'''
Takes as input a distribution pi and pretty prints it,
with the extra option of highlighting the maximum elements
'''

def print_dist(pi, highlight_maxima=False): 
    print("( ", end='')
    for p in pi:
        if highlight_maxima and p == max(pi):
            print("\033[1m%.2f\033[0m " % p, end='')
        else:
            print("%.2f " % p, end='')
    print(")")