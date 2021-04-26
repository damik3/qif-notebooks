import numpy as np

def get_G1():
    return np.array([
        [1, 0, 0, 0],
        [0, 100, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def get_G2():
    return np.array([
        [100, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 100, 0],
        [0, 0, 0, 100]
    ])
