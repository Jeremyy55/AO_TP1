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
    
    elem_to_del = 0
    
    solutions1 = tuple1.solution 
    solutions2 = tuple2.solution 
    
    comp_list = [-1 if obj1>obj2 else 0 if obj1==obj2 else 1 for obj1,obj2 in zip(solutions1,solutions2)]
    
    comp_set = set(comp_list)
    #print(comp_set)
    
    if all(x in comp_set for x in [0,1]) | ({1} == comp_set) :
        #print('on delete le 2e element : ' , tuple2)
        elem_to_del = 2
    
    elif (all(x in comp_set for x in [0,-1])) | ({-1} == comp_set) :
        #print('on delete le 1er element :', tuple1)
        elem_to_del = 1
         
    elif {0} == comp_set :
        #print('on ne supprime rien, les obj sont egaux :')
        elem_to_del = 0
        
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
    print('the dominated vector' , unique_domi)
    
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
            
def compare_old_and_new_archive(archive_old,archive_new) :
    
    equivalent_found = 0
    archive_changed = True;

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