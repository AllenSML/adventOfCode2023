import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input15.txt"
steps = open(str(cur_dir)+file_name).read().replace('\n', '').split(',')

sum = 0
map = dict()
boxes = defaultdict(list)

for step in steps:
    value = None    
    if "=" not in step:
        label = step[:-1]
        if label in map:
            boxnum, _ = map[label]
            del map[label]
            boxes[boxnum].remove(label)
            if len(boxes[boxnum]) == 0:
                del boxes[boxnum]
        continue
    
    label, value = step.split("=")
    boxNum = 0
    for ch in label:
        boxNum += ord(ch) 
        boxNum = (boxNum * 17) % 256
    if not label in map:
        boxes[boxNum].append(label)
    map[label] = (boxNum, value)    
        
sum = 0        
for id in boxes:
    for slot, label in enumerate(boxes[id]):
       sum += (id +1) * (slot + 1) * int(map[label][1])
       
print("part2: ", sum)        