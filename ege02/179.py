for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            f =  not(not x or not z) or (not x and not y or x and y)
            print(x, y, z, "|", int(f))