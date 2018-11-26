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


def get_solution(x, objs):
    """ je considère qu'on ne me donne que un vecteur de solution , et pas un vecteur de vecteur de solution."""
    obj_to_return = []
    for obj in objs:
        calcul = 0
        for i in range(len(x)):
            calcul += obj[i][x[i]]
        obj_to_return.append(calcul)
    return obj_to_return


if __name__ == '__main__':
    filepath = 'Data/'
    dim, obj = read_data(filepath+'LAP-8-2objSOL.dat')
    ini = init(dim, 3)
    print(f"""
        dim : {dim} 
        obj : {obj}
        init : {init}
    """)
    # create_namedtuple()
    for element in ini:
        print('solution \n :', get_solution(element, obj))
