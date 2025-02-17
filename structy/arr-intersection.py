def intersection(a, b):
    result = []
    my_set_b = set(a)

  
    
    for j in b:
        if j in my_set_b:
            result.append(j)

    return result






print(intersection([4,2,1,6], [3,6,9,2,10]))    