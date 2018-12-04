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