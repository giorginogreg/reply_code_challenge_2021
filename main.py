import os
import sys
import helpers as h
import grid as g

base_path = os.getcwd()

def read_file(input_file): 
    path = ''.join([base_path, '/', str(input_file)])
    grid = g.Grid(path)
    print(grid)
    
if __name__ == "__main__":
    read_file(sys.argv[1])