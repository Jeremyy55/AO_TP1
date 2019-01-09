from jer import Local_nadir
import GO
import numpy as np
from pprint import pprint


def bi_objectif():
    archive = [[2, 4], [3, 3], [5, 2]]
    reference = [7, 5]
    print(Local_nadir(archive, reference))


def tri_objectif():
    archive = [[3, 5, 7], [6, 2, 4], [4, 7, 3]]
    reference = [10, 10, 10]
    print('tri res: ', Local_nadir(archive, reference))


if __name__ == '__main__':
    print('debut')
    tri_objectif()
