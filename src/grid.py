def text_convert (fin, fout):
    dim = []

    finp = open (fin, "rb")
    foutp = open (fout, 'w')

    for i in range (0, 2):
        buff = int.from_bytes (finp.read (2), "little")
        dim.append (buff)
    
    print ("{} {}".format (dim[0], dim[1]), file=foutp)
    
    for i in range (1, dim[0] * dim[1] + 1):
        buff = int.from_bytes (finp.read (2), "little")

        if (i % dim[1] == 0):
            print ("{}".format (buff), file=foutp)
        
        else:
            print ("{} ".format (buff), file=foutp, end="")

    finp.close ()
    foutp.close ()

    return dim

def read (fname, dim):
    grid = []

    f = open (fname, "rb")
    f.read (4)

    for i in range (0, dim[0]):
        row = []
        for j in range (0, dim[1]):
            buff = int.from_bytes (f.read (2), "little")
            row.append (buff)
        grid.append (row)
    
    return grid

def write_p (ft, fname, path):
    nodes = 1
    start = [0, ft]

    f = open (fname, "w")

    print ("{}".format (path[start[0]][start[1]].time), file=f)

    px = path[start[0]][start[1]].px
    py = path[start[0]][start[1]].py

    while (px != -1 and py != -1):
        curr = path[px][py]
        nodes = nodes + 1

        px = curr.px
        py = curr.py

    print ("{}".format (nodes), file=f)
    print ("({}, {})".format (start[0], start[1]), file=f)

    px = path[start[0]][start[1]].px
    py = path[start[0]][start[1]].py

    while (px != -1 and py != -1):
        curr = path[px][py]
        print ("({}, {})".format (px, py), file=f)

        px = curr.px
        py = curr.py
    
    f.close ()


