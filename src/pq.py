from grid import *

class Heap:
    def __init__ (self, time, x, y):
        self.time = time
        self.x = x
        self.y = y

class Path: 
    def __init__(self, time, IN, px, py):
        self.IN = IN
        self.time = time

        self.px = px
        self.py = py 

def make_heap (dim, grid):
    pq = [None] * dim[0] * dim[1]

    for i in range (0, dim[1]):
        node = Heap (grid[dim[0] - 1][i], dim[0] - 1, i)
        pq[i] = node
    
    for i in range (1, dim[1]):
        up_heap (pq, i)

    v = dim[1]
    return v, pq

def down_heap (heap, i, n):
    tmp = heap[i]
    j = 2 * i + 1

    while (j <= n):
        if (j < n and (heap[j].time > heap[j + 1].time)):
            j = j + 1

        if (tmp.time <= heap[j].time):
            break

        else:
            heap[i] = heap[j]
            i = j
        
        j = 2 * i + 1
    
    heap[i] = tmp


def up_heap (heap, n):
    new = heap [n]
    child = n
    parent = (child - 1) // 2

    while (child > 0 and heap[parent].time > new.time):
        heap[child] = heap[parent]
        child = parent
        parent = (child - 1) // 2

    heap[child] = new

def extract (pq, path, v):
    min = pq[0]
    pq[0] = pq[v - 1]
    v = v - 1
    pq[v] = min

    down_heap (pq, 0, v - 1)
    path[min.x][min.y].IN = False
    return v, min
