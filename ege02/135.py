for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not y and x and (not z or w)
                print(x, y, z, w, "|", int(f))