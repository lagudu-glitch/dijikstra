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


from pq import *

def isADJ (r, c, dim):
    val = (r >= 0 and r < dim[0] and c >= 0 and c < dim[1])
    return val

def intialize (dim, grid):
    path = []

    for i in range (0, dim[0]):
        row = []

        for j in range (0, dim[1]):
            node = Path (None, None, None, None)

            if (i != dim[0] - 1):
                node.time = float ('inf')
            
            else:
                node.px = -1
                node.py = -1
                node.time = grid[i][j]
            
            node.IN = True
            row.append (node)
        
        path.append (row)
    
    return path

def dijkstra (dim, grid):
    cntr = 0
    fast = float ('inf')

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    path = intialize (dim, grid)
    vals = make_heap (dim, grid)

    v = vals[0]
    pq = vals[1]

    while (cntr != dim[1]):
        vals = extract (pq, path, v)
        v = vals[0]
        src = vals[1]

        if (src.x == 0):
            if (fast > src.time):
                ft = src.y
                fast = path[0][ft].time
            cntr = cntr + 1
        
        for i in range (0, 4):
            x = src.x + dx[i]
            y = src.y + dy[i]

            if (not (isADJ (x, y, dim))):
                continue

            if (not (path[x][y].IN)):
                continue

            if (path[x][y].time > src.time + grid[x][y]):
                time = src.time + grid[x][y]
                heapNode = Heap (time, x, y)
                pq[v] = heapNode

                path[x][y].px = src.x
                path[x][y].py = src.y
                path[x][y].time = time

                up_heap (pq, v)
                v = v + 1

    return ft, path 
