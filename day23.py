import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy
import sys

sys.setrecursionlimit(10000000)
cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input23.txt"
input = open(str(cur_dir)+file_name).read()
route = [list(line) for line in input.split("\n")]

di = dict(zip("^>v<", [(-1,0),(0,1),(1,0),(0,-1)]))
m, n, ans = len(route), len(route[0]), float("-inf")

def dfs(route, pos, visited):
    global ans
    if pos in visited:
        return 
    x, y = pos
    if x == m -1 and route[x][y] == ".": 
        ans = max(ans, len(visited))
        return         
    visited.add(pos)
    
    if route[x][y] in "^>v<":
        nx, ny = x + di[route[x][y]][0], y + di[route[x][y]][1]
        if (nx, ny) not in visited:
            if route[nx][ny] != "#":
                dfs(route, (nx,ny), visited.copy())
        return
    # do not mark the last tile if it is the exit
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        x_ = x + dx
        y_ = y + dy
        if (x_,y_) not in visited:
            if route[x_][y_] != "#":
                dfs(route, (x_,y_), visited.copy())
            
dfs(route, (0,1), set())
print("part1: ", ans)