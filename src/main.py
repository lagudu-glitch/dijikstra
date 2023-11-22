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
