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
