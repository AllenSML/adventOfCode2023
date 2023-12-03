import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input03.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

m = len(lines)
n = len(lines[0])
gears = defaultdict(list)   

def getNeigbours(x,y, nbs):
    currentNbs = [(x-1,y),(x+1,y),(x,y-1),(x,y+1), (x-1,y-1), (x+1,y+1), (x+1,y-1), (x-1,y+1)]    
    for dx, dy in currentNbs:
        if dx >= 0 and dx < m and dy >= 0 and dy < n:
            nbs.add((dx,dy))    

def isValidPart(nbs):
    for x, y in nbs:
        if lines[x][y] != '.' and not lines[x][y].isdigit():        
           return True,
    return False

def rememberGear(part, nbs):
    for x, y in nbs:
        if lines[x][y] == '*':        
           gears[(x,y)].append(part)


ans = 0
for row, line in enumerate(lines):
    part = ''
    nbs = set()

    for col, c in enumerate(line):
        if c.isdigit():
            part = part + c if part else c
            getNeigbours(row, col, nbs)
        elif not c.isdigit():
            if part:
                if isValidPart(nbs):
                    rememberGear(int(part), nbs)
                    ans += int(part)
                part = ''
            if nbs: nbs = set()
    else:
        if part:
            if isValidPart(nbs):
                rememberGear(int(part), nbs)
                ans += int(part)
        
print("part1:", ans)

ans = 0
for vals in gears.values():
    if len(vals) == 1: continue
    ans += functools.reduce(lambda x,y: x*y, vals)

print("part2:", ans)

    