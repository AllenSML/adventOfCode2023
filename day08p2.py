import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input08.txt"
parts = open(str(cur_dir)+file_name).read().split("\n\n")

nav = parts[0]
lines = parts[1].split("\n")
net = dict()

keys = []
for line in lines:
    key, left, right = re.findall(r"(\w+)", line)
    net[key] = (left, right)
    if key.endswith("A"):
        keys.append(key)

step = 0
stop = False
di = {"L": 0, "R": 1}
 
mem = dict()
for key in keys:     
    step = 0
    for direction in cycle(nav):    
        step += 1 
        key = net[key][di[direction]]
        if key[-1] == "Z":
            mem[(key)] = step
            break

lcm = 1
for val in mem.values():    
    lcm = lcm * val // math.gcd(lcm, val)
    
print("part2: ", lcm)