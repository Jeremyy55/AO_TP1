import numpy as np
from random import shuffle

from collections import namedtuple
from hypervolume.jer import domine_max, domine_min

Combo = namedtuple('Combo', 'x solution')


def create_combo(x, objs):
    return Combo(x=x, solution=get_solution(x, objs))


def avoid_double(archive):
    """
        convertis l'archive en un dictionnaire où la clef est le combo formaté en string. Comme une clef est unique, on supprime ainsi les doublons.
    """
    sol = dict()
    for a in archive:
        sol[str(a)] = a
    archive_doublon_free = []
    for key in sol.keys():
        archive_doublon_free.append(sol[key])
    return archive_doublon_free


def get_all_neighbour(x):
    x = np.array(x)
    l = len(x)
    permutations = []
    for i in range(l):
        for j in range(i+1, l):
            permutations.append([i, j])
    all_possible_permutations = []
    for permut in permutations:
        tmp = x.copy()
        tmp[permut] = x[permut[::-1]]
        all_possible_permutations.append(tmp.tolist())
    return all_possible_permutations


def add_potential(archive, potential_neighbour):
    """
        pour chacun des éléments dans les voisins potentiels,
        on parcours l'archive en entier. Si pour un seul élément de l'archive, p_n est dominé, on ne l'ajoute pas.
        si on l'ajoute après cela, on considère l'archive comme modifiée -> changed devient vrai
    """
    changed = False
    for p_n in potential_neighbour:
        # print('pp_n', p_n)
        add_me = True
        for a in archive:
            # print('a', a)
            if (a.x != p_n.x and domine_min(a.solution, p_n.solution)) or a.x == p_n.x:
                # print('dominated, donc add pn: ', p_n)
                add_me = False
        if add_me:
            changed = True
            # print('changed = ', changed,'car on vient d\'ajouter p_n =', p_n, '\n\n')
            archive.append(p_n)
    # cet étape n'est peut-être pas nécessaire, à vérifier.
    archive = avoid_double(archive)
    return archive, changed


def remove_dominated(archive):
    dominated = set()
    for i in range(len(archive)):
        for j in range(len(archive)):
            if i != j and domine_max(archive[i].solution, archive[j].solution):
                dominated.add(i)
    index_dominated = sorted(dominated)
    # print('dom:', index_dominated)
    for index in reversed(index_dominated):
        del archive[index]

    return archive


def read_data(filename):
    """
    fonction responsable de lire les données stockée dans les fichier .Dat donnés par le prof pour la séance de laboratoire
    """
    array = np.fromfile(filename, dtype=int, sep=' ')
    dim = array[0]
    obj = []
    for i in range(4):
        obj.append(array[1+i*dim**2:1+(i+1)*dim**2].reshape((dim, dim)))
    return dim, np.array(obj)


def init(dim, n=1):
    """
    initialisation de vecteur de solution random.
    prend en paramètre la dimension du vecteur et le nombre de solutions souhaitées.
    """
    ini = list()
    for i in range(n):
        tmp = [i for i in range(dim)]
        shuffle(tmp)
        ini.append(tmp)
    return ini


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
        init : {ini}
    """)
    # create_namedtuple()
    for element in ini:
        print('solution \n :', get_solution(element, obj))
