""" 
Copyright (c) 2023 Vishnu Lagudu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
"""


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


