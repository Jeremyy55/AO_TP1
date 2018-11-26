import numpy as np
from random import shuffle

from collections import namedtuple


def create_namedtuple():
    Combo = namedtuple('Combo', 'x solution')
    print('Type of combo: ', type(Combo))
    first_combo = Combo(x=[1, 2, 3], solution=60)
    second_combo = Combo([2, 3, 1], 785)
    print(first_combo.x, ' et ', first_combo.solution)
    print(second_combo.x, ' and ', second_combo.solution)


def read_data(filename):
    array = np.fromfile(filename, dtype=int, sep=' ')
    dim = array[0]
    obj = []
    for i in range(4):
        obj.append(array[1+i*dim**2:1+(i+1)*dim**2].reshape((dim, dim)))
    return dim, obj


def init(dim, n=1):
    init = list()
    for i in range(n):
        tmp = [i for i in range(dim)]
        shuffle(tmp)
        init.append(tmp)
    return init


if __name__ == '__main__':
    dim, obj = read_data('LAP-8-2objSOL.dat')
    init = init(dim, 3)
    print(f"""
        dim : {dim} 
        obj : {obj}
        init : {init}
    """)
    create_namedtuple()
