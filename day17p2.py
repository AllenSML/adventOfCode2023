import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input17.txt"
input = open(str(cur_dir)+file_name).read()
grid = list(map(list, input.split('\n')))

di = [(0,1), (-1,0), (0,-1), (1,0)] 
heap = [(0, 0, 0, 1), (0,0,0, 2)]
heapq.heapify(heap)


m = len(grid)
n = len(grid[0])
seen = set()
ans = 0
while heap:
    cost, x, y, d = heapq.heappop(heap)
    if (x, y, d) in seen:
        continue
    seen.add((x, y,d))
    if x == m - 1 and y == n - 1:
        ans = cost
        break      
    dl = (d + 1) % 4    
    dr = (d + 3) % 4    
    for dd in [dl, dr]:
        dx, dy = di[dd]
        loss = 0
        for step in range(1,11):
            x_, y_ = x + (dx * step), y + (dy * step)
            if x_ < 0 or x_ >= m or y_ < 0 or y_ >= n :
                continue
            loss += int(grid[x_][y_])
            if step < 4: continue
            heapq.heappush(heap, (loss+cost, x_, y_, dd))            
            
print("part 2: ", ans)