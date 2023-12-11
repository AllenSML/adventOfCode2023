import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

import sys

sys.setrecursionlimit(50000)

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input11.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

newLines = []
for line in lines:
    if line.count(".") == len(line):
        newLines.append(line)
    newLines.append(line)

lines = newLines
newLines = []
for line in zip(*lines):
    line = "".join(line)
    if line.count(".") == len(line):
        newLines.append(line)
    newLines.append(line)

grid = []
for line in zip(*newLines):
    grid.append("".join(line))

gal = list()
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "#":
            gal.append((i,j))            

res = 0
for x, y in combinations(gal, 2):
    dis = abs(x[0] - y[0]) + abs(x[1] - y[1])
    res += dis
    
print("part1: ", res)

