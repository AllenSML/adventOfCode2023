import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input16.txt"
input = open(str(cur_dir)+file_name).read()

grid = list(map(list, input.split('\n')))   
m = len(grid)
n = len(grid[0])    

# right, left down, up
directions = [(0,1), (0,-1), (1,0), (-1,0)] 
beams = deque([(0,0, directions[0])])
seen = set()
energized = set()

while beams:
    x, y, direction = beams.popleft()
    if (x,y, direction) in seen:
        continue
    seen.add((x,y, direction))   
    energized.add((x,y))
    direction_ = None
    if direction == directions[0]:
        if grid[x][y] == "\\":
            direction = directions[2]
        elif grid[x][y] == "/":
            direction = directions[3]
        elif grid[x][y] == "|":
            direction = directions[2]
            direction_ = directions[3]            
    elif direction == directions[1]:
        if grid[x][y] == "\\":
            direction = directions[3]
        elif grid[x][y] == "/":
            direction = directions[2]
        elif grid[x][y] == "|":
            direction = directions[2]
            direction_ = directions[3]           
    elif direction == directions[2]:
        if grid[x][y] == "\\":
            direction = directions[0]
        elif grid[x][y] == "/":
            direction = directions[1]
        elif grid[x][y] == "-":
            direction = directions[0]
            direction_ = directions[1]   
    elif direction == directions[3]:
        if grid[x][y] == "\\":
            direction = directions[1]
        elif grid[x][y] == "/":
            direction = directions[0]
        elif grid[x][y] == "-":
            direction = directions[0]
            direction_ = directions[1]   
    
    for dic in [direction, direction_]:
        if not dic: continue
        x_ = x + dic[0]
        y_ = y + dic[1]
        
        if 0 <= x_ < m and 0 <= y_ < n:
            beams.append((x_, y_, dic))     

print(len(energized))    
