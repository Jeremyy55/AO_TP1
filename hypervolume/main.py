from jer import Local_nadir
import GO
import numpy as np
from pprint import pprint


def read_data_in_solution_file(filename, dir_path='../nos_solutions/'):
    with open(dir_path+filename, 'r') as f:
        all_data = f.read().split('\n')
        file_len = len(all_data)-1
        xs = []
        for i in range(int(file_len/2)):
            xs.append(all_data[i].split(' ')[:-1])
        #print('xs:\n', xs)
        sols = []
        for i in range(int(file_len/2), file_len):
            sols.append(all_data[i].split(' ')[:-1])
        #print('sols:\n', sols)
    return xs, sols


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
    read_data_in_solution_file(filename)
