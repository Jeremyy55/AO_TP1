import numpy as np
from random import shuffle

from collections import namedtuple
from hypervolume.jer import domine_max, domine_min
import random

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

        


# Fonction pour trouver des voisins
# X est un vecteur représentant la position des 1
# nbNeighbour est le nombre de voisins qu'on veut créer
# Return une list de nouveaux voisins (sans doublon et ne comprenant pas le X de départ)


def find_neighbour(x):
    new_neighbour = x.copy()
    possible_element = [i for i in range(len(x))]
    row1 = possible_element.pop(random.randint(0, len(possible_element)-1))
    row2 = possible_element.pop(random.randint(0, len(possible_element)-1))
    new_neighbour[row1] = x[row2]
    new_neighbour[row2] = x[row1]
    return new_neighbour


def findNeighbours(X, nbNeighbour):
    neighbours = []
    for i in range(nbNeighbour):
        newNeighbour = X.copy()
        while True:
            row1 = int(round(random.random()*len(X))) % len(X)
            row2 = int(round(random.random()*len(X))) % len(X)
            tmp = newNeighbour[row1]
            newNeighbour[row1] = newNeighbour[row2]
            newNeighbour[row2] = tmp

            found = False
            for nb in neighbours:
                doublon = True
                for j in range(0, len(X)):
                    if nb[j] != newNeighbour[j]:
                        doublon = False
                if doublon == True:
                    found = True

            if not found:
                neighbours.append(newNeighbour)
                break
    return neighbours


def findNeighboursA(X, nbNeighbour, nPermut):
    neighbours = []
    for i in range(0, nbNeighbour):
        newNeighbour = X.copy()

        while True:

            permut_rows = random.sample(X, nPermut)

            temps = [newNeighbour[row] for row in permut_rows]

            for tmp, row in zip(reversed(temps), permut_rows):
                newNeighbour[row] = tmp

            found = False
            for nb in neighbours:
                doublon = True
                for j in range(0, len(X)):
                    if nb[j] != newNeighbour[j]:
                        doublon = False
                if doublon == True:
                    found = True

            if not found:
                neighbours.append(newNeighbour)
                break

    return neighbours
        
        

def x_and_sol_to_named_tuple(x_to_convert,objs) :
    
    """ Prend en entrée une liste de vecteurs X et 
    les associe à leurs solutions dans un named tuple 
    renvoit une liste de named_tuples """ 
    
    if (type(x_to_convert[0]) == list) :
        
        tuple_list = []
        for x in x_to_convert:
            x_tuple = Combo(x,get_solution(x,objs))
            tuple_list.append(x_tuple)

        return tuple_list
    
    else :
        
        return [Combo(x_to_convert,get_solution(x_to_convert,objs))]
    
 

def compare_two_points(tuple1,tuple2,) :
    
    """ return an integer 0, 1 , 2 to determine order of dominance
    0 : no dominance
    1 : the first element gets dominated
    2 : the second element gets dominated """
    
    #print("first tuple", tuple1)
    #print("second tupel",tuple2)
    elem_to_del = 0
    
    solutions1 = tuple1.solution 
    solutions2 = tuple2.solution 
    
    comp_list = [-1 if obj1>obj2 else 0 if obj1==obj2 else 1 for obj1,obj2 in zip(solutions1,solutions2)]
    
    comp_set = set(comp_list)
    #print(comp_set)
    
    if {0} == comp_set :
        #print('on ne supprime rien, les obj sont egaux :')
        elem_to_del = 0 
    
    elif all(x in [0,1] for x in comp_set) | ({1} == comp_set) :
        #print('on delete le 2e element : ' , tuple2)
        elem_to_del = 2
    
    elif (all(x in [0,-1] for x in comp_set)) | ({-1} == comp_set) :
        #print('on delete le 1er element :', tuple1)
        elem_to_del = 1
        
    else :
        #print('On ne supprime rien ')
        elem_to_del = 0
    
    return elem_to_del

def compare_and_delete(tuple_group) :
    
    """Compares each tuple to all the elements in the list,
    deletes the dominated ones,
    as well as the duplicates """

    dominated = []
    unique_domi = []
    unique_tuple_group = []
    tuple_group_copy = tuple_group.copy()
    
    ## creates a list of dominated tuples
    for (tuple1,tuple2) in itertools.combinations(tuple_group_copy,2):
             
            
            who_to_del = compare_two_points(tuple1,tuple2,)
         
            if who_to_del == 1 :
                dominated.append(tuple1)
            if who_to_del == 2 :
                dominated.append(tuple2)
                
    
    ## creates unique list of dominated tuples
    unique = [unique_domi.append(x) for x in dominated if x not in unique_domi]         
    #print('the dominated vector' , unique_domi)
    
    ## delete all the dominated tuples   
    tuple_group_copy[:] =  [n for n in tuple_group_copy if n not in unique_domi]
    
    ### delete all the duplicates in the tuple list  
    unique2 = [unique_tuple_group.append(x) for x in tuple_group_copy if x not in unique_tuple_group]
         
    return unique_tuple_group


def add_and_update_archive(neighbour_tuples, archive_tuple) :
    
    """ pour chaque nouvel élément potentiel, comparer cet élément à tout l'archive 
    Si l'élément domine un élément de l'archive, supprimer ce dernier et ajouter le nouvel élément
    Si l'élément se fait dominer au moins une fois, supprimer l'élement 
    Sinon, ajouter à l'archive."""
    
    who_to_del = 0 
    neigh_is_worse = False
    neighs_to_add = []
    unique_archive = []
   
    archive_tuple_copy = archive_tuple.copy()
    
    for neighbour in neighbour_tuples :
        
        
        
        for arch in reversed(archive_tuple_copy) : 
            
            #print('treating another arch')
            
                   
            who_to_del = compare_two_points(neighbour,arch)
            
            if who_to_del == 2 :
                
                #print("on va del qqun dans l'arch : ", arch)
                #print("celui qui l'a éliminé ", neighbour)
                archive_tuple_copy[:] = [x for x in archive_tuple_copy if x != arch]
            
            if who_to_del == 1 :
                #print(' issue : neighbour is worse than someone in the archive')
                neigh_is_worse = True
                break
                
        if neigh_is_worse == False :
            neighs_to_add.append(neighbour)
            
        neigh_is_worse = False
        
                
            #print('after boucle if \n')   
            #print(archive_tuple_copy)
    
    #print('neight to add : \n' ,neighs_to_add)
    archive_tuple_copy.extend(neighs_to_add)
    #print('full archive \n: ' , archive_tuple_copy)
    
    unique = [unique_archive.append(x) for x in archive_tuple_copy if x not in unique_archive]
    
    #print('type unique_arch ' , type(unique_archive))
    
    return unique_archive
            
def compare_old_and_new_archive(archive_old,archive_new) :
    
    equivalent_found = 0
    archive_changed = True;
    
    print('coucou')

    for new in archive_new :   
    
        for old in archive_old :    

            #print(old[0].x)
            #print(type(old))
            #print(new.x)

            if old.x == new.x :

                equivalent_found += 1
                continue;
    #print("number of equivalences found : ", equivalent_found)
    if (equivalent_found == len(archive_new) & len(archive_old) == len(archive_new)):
        archive_changed = False;

    #print('archive changed : '  , archive_changed)  
    

    return archive_changed 


def update_iterations_count(change,iterations_count):
  if change==False:
    iterations_count+=1
    #print(iterations_count)
  else:
    iterations_count=0
    #print(iterations_count)
  return iterations_count

def stop_condition(iterations_count,limite):
  if iterations_count > limite:
    return 0
  else:
    return 1   

if __name__== '__main__':
  import random
  iterations_count=0
  for i in range(120):
    iterations_count= update_iterations_count(True, iterations_count)
    # bool(random.getrandbits(1))
    test = stop_condition(iterations_count,50)  
    if test == False:
      break