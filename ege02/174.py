for x  in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not x or (y and z) or (y and not w) or (not z and not w)
                if not f:
                    print(x, y, z, w, "|", int(f))