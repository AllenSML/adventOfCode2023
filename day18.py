import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy
import sys
sys.setrecursionlimit(100000)

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input18.txt"
input = open(str(cur_dir)+file_name).read()
plans = [line.split() for line in input.split("\n")]

diMap = {"U":(0,-1),"D":(0,1),"R":(1,0),"L":(-1,0)}

grid = set()
pos = [0,0]
grid.add(tuple(pos))
grid.add(tuple(pos))
for di, number, colour in plans:
    number = int(number)
    for _ in range(number):
        pos[0] += diMap[di][0]
        pos[1] += diMap[di][1]
        grid.add(tuple(pos))

assert (0,0) in grid    
assert (1,1)  not in grid
print(len(grid))

def get_neighbours(x,y):
    return [(x-1,y), (x+1,y), (x,y+1), (x,y-1)]

def dfs(grid, pos, visited):
    assert pos not in grid
    if pos in visited:
        return 
    visited.add(pos)
    
    for x_, y_ in get_neighbours(*pos):        
        if not (x_,y_) in grid:
            dfs(grid, (x_,y_), visited)
            
            
stack = [(1,1)]
visited = set()
while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    for x_, y_ in get_neighbours(*current):
        if (x_,y_) not in grid:
            stack.append((x_,y_))
    
# visited = set()
# dfs(grid, (1,1), visited) 
print(len(visited)+len(grid))