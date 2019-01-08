import jer
import GO
import numpy as np

if __name__ == '__main__':
    print('debut')
    archive = [[2, 4], [3, 3], [5, 2]]
    reference = [7, 5]

    LNs = [reference]
    for arch in archive:
        new_LNs = []
        print('arch:', arch)
        for LN in LNs:
            print('LN', LN)
            if jer.domine_min(arch, LN):
                print(arch, ' domine ', LN)
                for element in jer.generate_from_domination(arch, LN):
                    new_LNs.append(element)
            else:
                new_LNs.append(LN)
        LNs = new_LNs
    print(LNs)
