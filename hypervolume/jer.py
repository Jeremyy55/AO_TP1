import numpy as np


def get_front(point, ensemble):
    pass


def domine_max(solution_1, solution_2):
    bool_domine = True
    for i in range(len(solution_2)):
        if solution_1[i] < solution_2[i]:
            bool_domine = False
            break
    return bool_domine


def domine_min(solution_1, solution_2):
    bool_domine = True
    for i in range(len(solution_2)):
        if solution_1[i] > solution_2[i]:
            bool_domine = False
            break
    return bool_domine


def generate_from_domination(solution_1, solution_2):
    generated = []
    for i in range(len(solution_1)):
        tmp = list(solution_2)  # copy
        tmp[i] = solution_1[i]
        generated.append(tmp)
    return generated
