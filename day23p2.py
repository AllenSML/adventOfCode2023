import os,math, difflib, pathlib, string, re, json, functools, networkx as ntx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy
import sys

sys.setrecursionlimit(10000000)

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input23.txt"
input = open(str(cur_dir)+file_name).read()
route = [list(line) for line in input.split("\n")]

m = len(route)
n = len(route[0])
print("m, n", m, n)

def nbs(i, j):    
    nb = [(i-1,j), (i+1,j), (i,j-1), (i,j+1) ]
    return [(nx,ny) for (nx, ny) in nb if 0 <= nx < m and 0 <= ny < n and route[nx][ny] != "#"]

cross = list()
for x in range(m):
    for y in range(n):
        if route[x][y] == "#":
            continue
        cnt = 0
        if len(nbs(x,y)) > 2:
            cross.append((x,y))

cross.append((0,1))
cross.append((m-1,n-2))
graph = defaultdict(dict)   

for x,y in cross:
    for nx, ny in nbs(x, y):
        prev, current = (x,y), (nx,ny)
        d = 1
        while current not in cross:
            
            prev, current = current, [nb for nb in nbs(*current) if nb != prev][0]
            d += 1
        graph[(x,y)][current] = d

seen = set()
def dfs(pos):
    if pos == (m-1, n-2):
        return 0
    ans = -float("inf")
    seen.add(pos)
    for key in graph[pos]:
        if key not in seen:
            ans = max(ans, dfs(key) + graph[pos][key]) 
    seen.remove(pos) 
    return ans

print(dfs((0,1)))