import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input14.txt"
lines = tuple(open(str(cur_dir)+file_name).read().split("\n"))

def tilt():
    global lines    
    for _ in range(4):
        newLines = list()
        for row in zip(*lines):
            start = -1        
            newRow = ["."] * len(row)
            for j, rock in enumerate(row):
                load = 0            
                if rock == "O":
                    start += 1
                    load = start            
                    newRow[load] = "O"
                elif rock == "#":
                    start = j     
                    newRow[j] = rock   
                        
            newLines.append("".join(newRow[::-1]))
        lines = tuple(newLines)

    return lines

visited = {lines}
array = [lines]

it = 0

while True:
    it += 1
    tilt()
    if lines in visited:
        break
    visited.add(lines)
    array.append(lines)
    
id = array.index(lines)
    
index = (1000000000 - id) % (it - id)
first = index + id
lines = array[first]

print(sum(row.count("O") * (len(lines) - i) for i, row in enumerate(lines)))