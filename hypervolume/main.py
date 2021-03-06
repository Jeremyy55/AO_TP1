from jer import Local_nadir, domine_min
from GO import compute_hypervolum_surface
import numpy as np
from pprint import pprint
import scipy.io as io


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


def compare_solutions_and_get_dominance(sols1, sols2):
    print('longueur 1:', len(sols1))
    print('longueur 2:', len(sols2))

    total_solutions = sols1+sols2
    dominated = set()
    for i in range(len(total_solutions)):
        for j in range(len(total_solutions)):
            if i != j and domine_min(total_solutions[i], total_solutions[j]):
                #j is dominated
                dominated.add(j)
    # maintenant qu'on a qui est dominé
    to_remove = list(dominated)
    to_remove.sort()  # trié par odre croissant
    # parce que faut supprimer du plus grand indice jusqu'au plus petit sinon ça fait n'importe quoi
    for index in reversed(to_remove):
        del total_solutions[index]
    # maintenant qu'on a juste les non dominés:
    print('taille totale de l\'ensemble: ', len(total_solutions))
    survivor1 = [element for element in sols1 if element in total_solutions]
    survivor2 = [element for element in sols2 if element in total_solutions]
    print('nombre de survivant chez le premier ensemble:', len(survivor1))
    print('nombre de survivant chez le second ensemble:', len(survivor2))


def compute_ref(sols):
    reference = sols[-1]
    for sol in sols[:-1]:
        for i in range(len(reference)):
            if sol[i] > reference[i]:
                reference[i] = sol[i]
    for i in range(len(reference)):
        reference[i] = int(1.10*reference[i])
    return reference


def read_AJ_AR(dir_used, filename='AJ_AR.mat', dir_path='../solutions_autres/'):
    total_path = dir_path+dir_used+filename
    print('total path:', total_path)
    mat = io.loadmat(dir_path+dir_used+filename)
    xs = mat['A']
    sols = mat['A_obj']
    return xs.tolist(), sols.tolist()


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
    xs_a, sols_a = read_AJ_AR('15-4obj/')
    filename = 'quinzex15_4obj.txt'
    xs, sols = read_data_in_solution_file(filename)
    compare_solutions_and_get_dominance(sols, sols_a)
    # prenez bien le même fichier sinon ça va pas aller
    """
    reference_nous = compute_ref(sols)
    reference_a = compute_ref(sols_a)
    final_ref = []
    for i in range(len(reference_nous)):
        if reference_a[i] > reference_nous[i]:
            final_ref.append(reference_a[i])
        else:
            final_ref.append(reference_nous[i])
    LN_nous = Local_nadir(sols, final_ref)
    LN_a = Local_nadir(sols_a, final_ref)
    print('local Nadir:\n', LN_nous)
    list_z = []
    for i in range(len(final_ref)):
        tmp = [0 for i in range(len(final_ref))]
        tmp[i] = final_ref[i]
        list_z.append(tmp)
    hp_nous = compute_hypervolum_surface(LN_nous, final_ref, list_z+sols)
    hp_a = compute_hypervolum_surface(LN_a, final_ref, list_z+sols_a)
    print('hyper volume nous: ', hp_nous)
    print('hyper volume a: ', hp_a)

    print('ref:', final_ref)
    """
