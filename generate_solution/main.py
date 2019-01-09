import anissa
import julie
from gauthier import stop_condition, update_iterations_count
from jeremy import read_data, init, get_solution

if __name__ == '__main__':
    # lecture des tableaux et initialisation des premiers vecteurs x

    print('debut')
    filepath = 'Data/'
    filename = 'LAP-8-2objSOL.dat'
    dim, obj = read_data(filepath+filename)
    xs = init(dim, 3)
    iteration_count = 0
    while stop_condition(iteration_count, 100):
        print(iteration_count)
        iteration_count = update_iterations_count(False, iteration_count)
    print('fin')
