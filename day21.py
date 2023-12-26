import os,math, difflib, pathlib, string, re, json, functools, networkx as ntx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy
import sys

sys.setrecursionlimit(10000000)
cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input21.txt"
input = open(str(cur_dir)+file_name).read()
grid = [list(line) for line in input.split("\n")]

m = len(grid)
n = len(grid[0])

print("totla sum ", m * n, m,  )
start = None
for i in range(m):
    for j in range(n):
        if grid[i][j] == "S":
            start = (i,j)

queue = deque([start])    

occupied = set()
step = 0
count = set()
pattern = list()
found = False

while queue:        
    if step ==  50:
        break
    occupied = set()        
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            mnx = nx % m
            mny = ny % n
            # if not 0 <= nx < m and 0 <= ny < n:
                # print("break:", step)
                # exit()
            # if 0 <= nx < m and 0 <= ny < n and  grid[nx][ny] != "#" and (nx, ny) not in occupied:
            if grid[mnx][mny] != "#" and (nx, ny) not in occupied:
                queue.append((nx, ny))
                occupied.add((nx,ny))
    
    print(step, len(occupied), len(queue))        
    
    if len(occupied) in count:
        pattern = pattern[pattern.index(len(occupied)):]
        break
    else:
        count.add(len(occupied))
    pattern.append(len(occupied))
        
    step += 1

print(len(occupied))    
print(pattern)


