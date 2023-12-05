import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input05.txt"
parts = open(str(cur_dir)+file_name).read().split("\n\n")

seeds = list(map(int,parts[0].strip().split()[1:]))

res = float("inf")
for current in seeds:
    current = int(current)

    for i, part in enumerate(parts[1:]):        
        for line in part.split("\n")[1:]:
            (des, origin, length) = list(map(int,line.split()))
            if current >= origin and current < origin + length:
                current = des + (current - origin)
                break
    res = min(res, current)
    
print(res)
            
            
        
    
    
        
    
    
