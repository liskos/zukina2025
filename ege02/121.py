for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (not x and y and z) or (not x and y and not z) or (not x and not y and not z)
            print(x, y, z, "|", int(f))