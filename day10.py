import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

import sys

sys.setrecursionlimit(50000)

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input10.txt"
grid = open(str(cur_dir)+file_name).read().split("\n")

def recursive_traversal(grid, r, c, loop):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in loop:
        return

    ch = grid[r][c]
    loop.add((r, c))

    if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F":
        recursive_traversal(grid, r - 1, c, loop)
    if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL":
        recursive_traversal(grid, r + 1, c, loop)
    if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF":
        recursive_traversal(grid, r, c - 1, loop)
    if c < len(grid[0]) - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7":
        recursive_traversal(grid, r, c + 1, loop)

sr, sc = -1, -1
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "S":
            sr, sc = r, c
            break
    else:
        continue
    break

loop = set()
recursive_traversal(grid, sr, sc, loop)
print(len(loop) // 2)
