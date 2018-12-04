import numpy as np


def get_front(point, ensemble):
    pass


def domine(solution_1, solution_2):
    bool_domine = True
    for i in range(len(solution_2)):
        if solution_1[i] < solution_2[i]:
            bool_domine = False
            break
    return bool_domine
