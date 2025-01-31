def parallel(list_of_resistances):
    total = (1/(list_of_resistances[0]))+((1/(list_of_resistances[1]))+((1/list_of_resistances[2])))
    parallel_resistance = 1/total
    print("{:.3f}".format(parallel_resistance)+" ohms")
        
        
list =[330, 1000, 2200]

parallel(list)
 
