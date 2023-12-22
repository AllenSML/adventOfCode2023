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
    
def main(beams):
    seen = set()
    energized = defaultdict(int)
    while beams:
        x, y, direction = beams.popleft()
        if (x,y, direction) in seen:
            continue
        seen.add((x,y, direction))   
        energized[(x,y)] += 1
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

    return len(energized)
    
ans = float("-inf")
for i, rol in enumerate(grid):
    for j, ch in enumerate(rol):    
        if i == 0 or i == m-1 or j == 0 or j == n-1:                        
            if i == 0:
                beams = deque([(i,j, directions[2])])
                ans = max(ans, main(beams))
            if i == m-1:    
                beams = deque([(i,j, directions[3])])
                ans = max(ans, main(beams))
            if j == 0:
                beams = deque([(i,j, directions[0])])
                ans = max(ans, main(beams))
            if j == n-1:
                beams = deque([(i,j, directions[1])])
                ans = max(ans, main(beams))

print("part2: ", ans)                