for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = not(x or y) or (not y and not z or y and z)
            print(x, y, z, "|", int(f))