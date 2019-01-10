from jer import Local_nadir
from GO import compute_hypervolum_surface
import numpy as np
from pprint import pprint


def read_data_in_solution_file(filename, dir_path='../nos_solutions/'):
    with open(dir_path+filename, 'r') as f:
        all_data = f.read().split('\n')
        file_len = len(all_data)-1
        xs = []
        for i in range(int(file_len/2)):
            tmp = [int(value) for value in all_data[i].split(' ')[:-1]]
            xs.append(tmp)
        #print('xs:\n', xs)
        sols = []
        for i in range(int(file_len/2), file_len):
            tmp = [int(value) for value in all_data[i].split(' ')[:-1]]
            sols.append(tmp)
        #print('sols:\n', sols)
    return xs, sols


def compute_ref(sols):
    reference = sols[-1]
    for sol in sols[:-1]:
        for i in range(len(reference)):
            if sol[i] > reference[i]:
                reference[i] = sol[i]
    for i in range(len(reference)):
        reference[i] = int(1.10*reference[i])
    return reference


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
    # tri_objectif()
    filename = 'trentex30_2obj.txt'
    xs, sols = read_data_in_solution_file(filename)
    reference = compute_ref(sols)
    LN = Local_nadir(sols, reference)
    print('local Nadir:\n', LN)
    list_z = []
    for i in range(len(reference)):
        tmp = [0 for i in range(len(reference))]
        tmp[i] = reference[i]
        list_z.append(tmp)
    hp = compute_hypervolum_surface(LN, reference, list_z)
    print(hp)
