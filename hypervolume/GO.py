#def calcul_hypervolume(input):



def point_reference(solution):
    size = len(solution[0][1])
    reference=[]
    for i in range(size):
        reference.append(-sys.maxsize)

    print(reference)
    for element in solution:
        print(element)
        for i in range(len(element)):
            if i%2!=0:
                for j,objectif in enumerate(element[i]):
                    if objectif > reference[j]:
                        print(objectif)
                        reference[j]=objectif
                        print("références : ", reference[i])
    return reference
if __name__=="__main__":
    import sys
    point_reference([([1,2],[18,24]),([2,4],[36,47]),([1,2],[25,48]),([1,2],[36,47])])        