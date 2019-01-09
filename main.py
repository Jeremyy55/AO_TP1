import anissa
from julie import find_neighbour
from gauthier import stop_condition, update_iterations_count
from jeremy import read_data, init, get_solution, create_combo, remove_dominated, avoid_double, add_potential, get_all_neighbour
from time import sleep


if __name__ == '__main__':
    # lecture des tableaux et initialisation des premiers vecteurs x

    print('debut')
    filepath = 'Data/'
    filename = 'LAP-8-2objSOL.dat'
    # lecture des données utile dans le fichier
    dim, obj = read_data(filepath+filename)
    number_of_objectif = 4
    objs = obj[:number_of_objectif]
    # initialisation de solutions et création de l'archive
    xs = init(dim, 3)
    archive = []
    for x in xs:
        archive.append(create_combo(x, objs))
    #print('archive', archive)
    archive = remove_dominated(archive)
    #print('archive', archive)

    # début de la recherche
    iteration_count = 0
    n_neighbours_by_it = 5
    n_deeper = 3

    while stop_condition(iteration_count, 20):
        # on réinitialise les voisins potentiels
        potential_neighbour = []

        for element in archive:
            # pour chaque élement, n_neighbours_by_it fois
            for voisins in get_all_neighbour(element.x):
                potential_neighbour.append(create_combo(voisins, objs))

            """
            for unused_variable in range(n_neighbours_by_it):
                # divergence proche
                neighbour = find_neighbour(element.x)
                potential_neighbour.append(create_combo(neighbour, objs))
                for another_unused_variable in range(n_deeper):
                    # et on diverge sur n_deeper niveaux
                    neighbour = find_neighbour(neighbour)
                    potential_neighbour.append(create_combo(neighbour, objs))"""

        # on conserve les non-dominé
        #print('\n avant le remove dom+avoid double\n')
        potential_neighbour = remove_dominated(
            avoid_double(potential_neighbour))
        #print('\npotential_neighbour updated\n', potential_neighbour)
        # sleep(2)
        #print('potential', potential_neighbour)
        archive, changed = add_potential(archive, potential_neighbour)
        #print('changed: ', changed)
        #print('\narchive + potential: \n', archive)
        # sleep(2)
        archive = remove_dominated(archive)
        #print('changed:', changed)
        #print('archive', archive)
        iteration_count = update_iterations_count(changed, iteration_count)
        print(iteration_count)
    print('fin')
    # print(archive)
    a = set()
    for element in archive:
        a.add(str(element.solution))
    print(len(a), 'solution\n')
    for el in a:
        print(el)
