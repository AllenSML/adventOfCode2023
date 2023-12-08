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

for line in lines:
    key, left, right = re.findall(r"(\w+)", line)
    net[key] = (left, right)

key = "AAA"
step = 0
for direction in cycle(nav):    
    key = net[key]["LR".index(direction)] 
    step += 1
    if key == "ZZZ":        
        break

print("part1: ", step)
    



    
    



