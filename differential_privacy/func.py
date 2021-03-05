import numpy as np
import collections


def get_db(id_db, num_persons, num_values, values):
    db = [None for i in range(num_persons)]
    for i in range(num_persons):
        db[num_persons - 1 - i] = values[id_db % num_values]
        id_db -= id_db % num_values
        id_db /= num_values
        id_db = int(id_db)
    return db


def f(db, value):
    c = collections.Counter(db)
    return c[value]


def get_c(j, m, a):
    if j == 0 or j == m-1:
        return 1/(1+a)
    elif 0 < j < m-1:
        return (1-a) / (1+a)
    
    
def get_h(i, j, n, m, a):
    return get_c(j, m, a) * (a ** abs(i-j))


def get_C(num_persons, values, value):
    a = 1/3
    num_values = len(values)
    
    C = np.zeros((num_values ** num_persons, num_values+1))
    
    for i in range(num_values ** num_persons):
         for j in range(num_values+1):
             C[i][j] = get_h(f(get_db(i, num_persons, num_values, values), value), j, num_persons, num_values+1, a)
    
    return C


def get_H(n, m, a):
    return np.array([[get_h(i, j, n, m, a) for j in range(m)] for i in range(n)])

