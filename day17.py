import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input17.txt"
input = open(str(cur_dir)+file_name).read()
grid = list(map(list, input.split('\n')))

di = [(0,1), (-1,0), (0,-1), (1,0)] 
#cost, x, y, di
heap = [(0, 0, 0, 1), (0,0,0, 2)]
heapq.heapify(heap)


m = len(grid)
n = len(grid[0])
seen = set([(0,0)])
ans = 0
while heap:
    cost, x, y, d = heapq.heappop(heap)
    print(cost, x,y, grid[x][y], d )
    if x == m - 1 and y == n - 1:
        # print(heap)
        # print("......", cost, x, y)
        ans = cost
        break      
    dl = (d + 1) % 4    
    dr = (d + 3) % 4    
    for dd in [dl, dr]:
        dx, dy = di[dd]
        for step in [1,2,3]:
            x_, y_ = x + (dx * step), y + (dy * step)
            if x_ < 0 or x_ >= m or y_ < 0 or y_ >= n or (x_, y_) in seen:
                continue
            # print("----", int(grid[x_][y_]), cost, int(grid[x_][y_]) + cost)
            if x_ == 12 or y_ == 12:
                print("----", int(grid[x_][y_]), cost, int(grid[x_][y_]) + cost)
                
            heapq.heappush(heap, (int(grid[x_][y_])+cost, x_, y_, dd))            
            seen.add((x_, y_))


print("paert 1: ", ans)