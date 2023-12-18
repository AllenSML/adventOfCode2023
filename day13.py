import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input13.txt"
patterns = open(str(cur_dir)+file_name).read().split("\n\n")

def find_reflection(pattern):
    for i in range(len(pattern)-1):
        left = pattern[:i+1][::-1]
        right = pattern[i+1:]
        matched = all( l == r for (l, r) in zip(left, right))
        if matched:
            return True, i+1
    return False, 0

ans = 0
for pattern in patterns:
    pattern = pattern.split("\n")
    found, numOfCol = find_reflection(pattern)      
    if found: 
        ans += 100 * numOfCol
        print("found horizontal reflection at: ", numOfCol)
        continue
    cols = ["".join(col) for col in zip(*pattern)]
    found, numOfCol = find_reflection(cols)  
    if found:
        ans += numOfCol
        
print(ans)