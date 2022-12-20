def jumpingOnClouds(c):
    move = 0 
    i = 0
    while i < len(c)-1:
        if i+2<len(c) and c[i+2] !=1:
            i += 2
            move += 1 
        else:
            i += 1
            move += 1
      

    return move        
                    