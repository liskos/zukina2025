for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (not y or x) and z and not(not z and not y or z and y)
            print(x, y, z, "|", int(f))