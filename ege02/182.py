for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (x or y) and not z and not(not z and not x or z and x)
            print(x, y, z, "|", int(f))