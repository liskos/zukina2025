for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f =  ((not x or z) and (not z or w)) or (not y and not (x or z) or y and (x or z))
                print(x, y, z, w, "|", int(f))