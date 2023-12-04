import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input04.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

res = 0
c2n = [ 1 for _ in range(len(lines))]

for id, line in enumerate(lines):
    p_ = len(functools.reduce(lambda x,y: x & y,   [set(p.strip().split()) for p in line.split(":")[1].strip().split("|")]))
    res = res + (2**(p_-1) if p_ > 0 else 0)
    for _ in range (p_):
        c2n[_+1+id] += 1 * c2n[id]

print("part1:", res)
print("part2:", sum(c2n))
