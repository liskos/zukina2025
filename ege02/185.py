for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not x and not y and not z or y and z) and w
                print(x, y, z, w, "|", int(f))