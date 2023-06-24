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


from time import time
from dijkstra import *

def main ():
    file = str (input ("Please enter your binary file: "))
    text = str (input ("Please enter output text file: "))
    fast = str (input ("Please enter output path file: "))

    dim = text_convert (file, text)
    grid = read (file, dim)

    start = time()
    (ft, path) = dijkstra (dim, grid)
    end = time()

    write_p (ft, fast, path)
    print ("Time taken: {}".format (end - start))

if __name__ == "__main__":
    main ()