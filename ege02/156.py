for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (not x or not z) and (y or not x)
            print(x, y, z, "|", int(f))