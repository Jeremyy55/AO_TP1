import numpy as np


def Local_nadir(archive, reference):
    LNs = [reference]
    for arch in archive:
        tmp_LNs = []
        for LN in LNs:
            if domine_min(arch, LN):
                for element in generate_from_domination(arch, LN):
                    tmp_LNs.append(element)
            else:
                tmp_LNs.append(LN)

        dominator = []
        for i in range(len(tmp_LNs)):
            for j in range(len(tmp_LNs)):
                if domine_min(tmp_LNs[i], tmp_LNs[j]) and tmp_LNs[j] != tmp_LNs[i]:
                    dominator.append(i)
        for index in reversed(dominator):
            del tmp_LNs[index]
        LNs = tmp_LNs
    return LNs


def get_front(point, ensemble):
    pass


def domine_max(solution_1, solution_2):
    """
        pour chaque solution dans le vecteur de solution: 
        1) je compare si la solution 1 est plus petite que la solution 2. Si c'est le cas, elle ne peut pas dominer.
        2) je regarde si les valeurs sont différentes. si c'est le cas, impossible que toutes les valeurs soit égales.

        à la fin: 
            si toutes les valeurs sont égales, sol1 ne domine pas
            sinon, retourne Vrai si sol1 domine , False sinon
    """
    bool_domine = True
    all_equal = True
    for i in range(len(solution_2)):
        if solution_1[i] < solution_2[i]:
            bool_domine = False
            break
        elif solution_1[i] != solution_2[i]:
            all_equal = False
    if all_equal:
        return False
    else:
        return bool_domine


def domine_min(solution_1, solution_2):
    bool_domine = True
    all_equal = True
    for i in range(len(solution_2)):
        if solution_1[i] > solution_2[i]:
            bool_domine = False
            break
        elif solution_1[i] != solution_2[i]:
            all_equal = False
    if all_equal:
        return False
    else:
        return bool_domine


def generate_from_domination(solution_1, solution_2):
    generated = []
    for i in range(len(solution_1)):
        tmp = list(solution_2)  # copy
        tmp[i] = solution_1[i]
        generated.append(tmp)
    return generated
