for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            f =  not(not z or not y) or (not x and not z or x and z)
            print(x, y, z, "|", int(f))