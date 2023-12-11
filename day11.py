import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input11.txt"
lines = open(str(cur_dir)+file_name).read().splitlines()

erow = [ i for i, l in enumerate(lines) if l.count(".") == len(l)]
ecol = [ i for i in range(len(lines[0])) if all(l[i] == "." for l in lines)]
gal = [(i,j) for i, row in enumerate(lines) for j, col in enumerate(row) if col == "#"]

def calculate(expand):
    res = 0
    for x, y in combinations(gal, 2):
        sr = min(x[0], y[0])
        br = max(x[0], y[0])
        sc = min(x[1], y[1])    
        bc = max(x[1], y[1])    
        res += sum(expand if sr < r < br else 0 for r in erow)
        res += sum(expand if sc < c < bc else 0 for c in ecol)            
        dis = abs(x[0] - y[0]) + abs(x[1] - y[1])
        res += dis
    return res

expand = 1
res = calculate(expand)
print("part1: ", res)

expand = 1000000 - 1
res = calculate(expand)
print("part2: ", res)