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
