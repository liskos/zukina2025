for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x and z) or (not(not w or x) and not (not z or y) or (not w or x) and (not z or y))
                print(x, z, y, w, "|", int(f))