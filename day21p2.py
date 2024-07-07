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
preCnt = 1


while queue:        
    if step ==  200:
        break
    occupied = set()        
    occupied2 = set()        
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            # if 0 <= nx < m and 0 <= ny < n and  grid[nx][ny] != "#" and (nx, ny) not in occupied:                
                # occupied2.add((nx,ny))
            mnx = nx % m
            mny = ny % n
            # if 0 <= nx < m and 0 <= ny < n and  grid[nx][ny] != "#" and (nx, ny) not in occupied:
            
            if grid[mnx][mny] != "#" and (nx, ny) not in occupied:
                if -55 <= nx < 55 and -55 <= ny < 55:
                    occupied2.add((nx,ny))
                    
                queue.append((nx, ny))
                occupied.add((nx,ny))
    
    
    curCnt = len(occupied)
    # pattern.append(curCnt - preCnt)
    pattern.append(curCnt)
    print(step, curCnt, len(queue), curCnt - preCnt, len(occupied2))
    preCnt = curCnt
    
    
    
    
    step += 1

print(len(occupied))    
print(pattern)

# print("------------------")
# for i in range(len(pattern)):
#     if i % 10  == 0:
#         print(i, pattern[i])        


