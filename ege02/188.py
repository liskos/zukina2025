for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f =  (w and y) or (not(not x or w) and not(not y or z)or (not x or w) and (not y or z) )
                print(x, y, z, w, "|", int(f))