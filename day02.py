import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input02.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

c2cnt = {"red": 12, "green": 13, "blue": 14}
ans = 0
for line in lines:
    p1, p2 = line.split(":")
    id = p1.split()[1]
    groups = p2.split(";")

    valid = True
    for group in groups:
        for pair in group.strip().split(","):
            cnt, color = pair.strip().split()
            if int(cnt) > c2cnt[color]:
                valid = False
                break            
        if not valid:
            break
    else:
        ans += int(id)
    
print("part1:", ans)   

ans = 0
for line in lines:
    p1, p2 = line.split(":")
    id = p1.split()[1]
    groups = p2.split(";")

    valid = True
    c2cnt = {"red": 0, "green": 0, "blue": 0}

    for group in groups:
        for pair in group.strip().split(","):
            cnt, color = pair.strip().split()
            c2cnt[color] = max(c2cnt[color], int(cnt))
                
    ans +=functools.reduce(lambda x, y: x*y, c2cnt.values())

print("part2:", ans)