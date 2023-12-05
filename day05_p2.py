import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input05.txt"
parts = open(str(cur_dir)+file_name).read().split("\n\n")

seeds = list(map(int,parts[0].strip().split()[1:]))

seedPairs = list()
for i in range(0,len(seeds),2):    
        seedPairs.append((seeds[i],seeds[i]+ seeds[i+1] + 1))

print(seedPairs)
res = float("inf")

for pair in seedPairs:
    nextPairs = [pair]
    for _, part in enumerate(parts[1:]):                    
        currentPairs = nextPairs.copy()        
        nextPairs = list()                
        while currentPairs:
            l, r = currentPairs.pop()               
            for line in part.split("\n")[1:]:
                (des, origin, length) = list(map(int,line.split()))
                length -= 1
                if origin <= l <= r <= origin + length:
                    nextPairs.append((l + (des - origin), r + (des - origin)))
                    break
                elif origin <= l <= origin + length:
                    currentPairs.append((origin + length +1 , r))
                    nextPairs.append((l + (des - origin), des + length))
                    break
                elif origin <= r <= origin + length:                    
                    if l < origin:      
                        currentPairs.append((l, origin-1))
                        nextPairs.append((des, r + (des - origin) ))
                    break
            else:
                nextPairs.append((l,r))
    
    res = min(res, min(i for i, j in nextPairs))

print("part2:", res)
    
    

