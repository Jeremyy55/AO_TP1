def x_and_sol_to_named_tuple(x_to_convert,objs) :
    
    """ Prend en entrée une liste de vecteurs X et 
    les associe à leurs solutions dans un named tuple 
    renvoit une liste de named_tuples """ 
    
    if (type(x_to_convert[0]) == list) :
        
        tuple_list = []
        for x in x_to_convert:
            print(x)
            print(x[0])
            x_tuple = Combo(x,get_solution(x,objs))
            tuple_list.append(x_tuple)

        return tuple_list
    
    else :
        
        return Combo(x_to_convert,get_solution(x_to_convert,objs))
    
 

def compare_two_points(tuple1,tuple2,) :
    
    """ return an integer 0, 1 , 2 to determine order of dominance
    0 : no dominance
    1 : the first element gets dominated
    2 : the second element gets dominated """
    
    elem_to_del = 0
    
    solutions1 = tuple1.solution 
    solutions2 = tuple2.solution 
    
    comp_list = [-1 if obj1>obj2 else 0 if obj1==obj2 else 1 for obj1,obj2 in zip(solutions1,solutions2)]
    
    comp_set = set(comp_list)
    #print(comp_set)
    
    if all(x in comp_set for x in [0,1]) | ({1} == comp_set) :
        print('on delete le 2e element : ' , tuple2)
        elem_to_del = 2
    
    elif (all(x in comp_set for x in [0,-1])) | ({-1} == comp_set) :
        print('on delete le 1er element :', tuple1)
        elem_to_del = 1
         
    elif {0} == comp_set :
        print('on ne supprime rien, les obj sont egaux :')
        elem_to_del = 0
        
    else :
        print('On ne supprime rien ')
        elem_to_del = 0
    
    return elem_to_del


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
                print("on va del qqun dans l'arch : ", arch)
                archive_tuple_copy[:] = [x for x in archive_tuple_copy if x != arch]
            
            if who_to_del == 1 :
                print(' issue : neighbour is worse than someone in the archive')
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
    
    #print('normally unique arch ' , unique_archive)
    
    return unique_archive
            