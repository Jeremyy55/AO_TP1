#def calcul_hypervolume(input):
import numpy as np


def point_reference(solution):
    size = len(solution[0][1])
    reference=[]
    for i in range(size):
        reference.append(-sys.maxsize)

    #print(reference)
    for element in solution:
        print(element)
        for i in range(len(element)):
            if i%2!=0:
                for j,objectif in enumerate(element[i]):
                    if objectif > reference[j]:
                        #print(objectif)
                        reference[j]=objectif
                        #print("références : ", reference[i])
    return reference



def compute_hypervolum_surface(LN,reference_point,list_z):
    """
    Fonction retournant la valeur de la surface de l'hypervolume

    Parameters
    ----------
    LN: list 
        contient les nadir point
    reference_point: list
        point de référence
    list_z: list 
        contient les dummy points et les points de l'archive

    Returns
    -------
    int
        Surface de l'hypervolume
    """
    surface = 0
    for value in LN:
        #print(len(value))
        #permet de créer le vecteur contenant les projections du point selon tous les axes
        points_projection=[]
        for i in range(len(value)):
            for z in list_z:
                if value[i]==z[i]:
                    points_projection.append(z)
        valeurs=[]
        #première partie de l'équation B(u)
        for i in range(len(value)):
            if i == 0:
                valeurs.append([value[0],reference_point[0]])
                first_value = reference_point[0]-points_projection[0][0]
                #print("first_value: ",first_value)
            #Deuxième partie de l'équation B(u)
            else:
                tmp = []

                #print("points: ",points_projection)    
                tmp = points_projection[:i]
                tmp = max(tmp, key=lambda item: item[i])
                #print("tmp: ",tmp, i)
                valeur = [tmp[i], value[i]]
                valeurs.append(valeur)
        #print(valeurs)
        #multiplication des différences des vecteurs obtenues dans le vecteur des valeurs
        valeurs = np.array(valeurs)
        tmp_value = 1
        for value in valeurs:
            tmp_value= tmp_value*np.diff(value)         
        #print("wtf",tmp_value)
        surface+=tmp_value
    return int(surface)   
if __name__=="__main__":
    import sys
    test = compute_hypervolum_surface([[3,10,10],[6,5,10],[10,2,10],[4,10,7],[6,7,7],[10,7,4],[10,10,3]],[10,10,10],[[3,5,7],[6,2,4],[4,7,3],[10,0,0],[0,10,0],[0,0,10]])
    print("test: ",test)
    test = compute_hypervolum_surface([[2,5],[3,4],[5,3],[7,2]],[7,5],[[7,0],[0,5],[3,3],[2,4],[5,2]])
    print("test: ",test)
    # ref = point_reference([([1,2],[18,24]),([2,4],[36,47]),([1,2],[25,48]),([1,2],[36,47])])       
    # print(ref)
     