import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input14.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

rowCnt = len(lines)
res = 0

def tilt(lines):
    global res
    for i, col in enumerate(zip(*lines)):
        start = -1
        for j, rock in enumerate(col):
            load = 0
            if rock == "O":
                start += 1
                load = start            
                res += (rowCnt - load) 
            elif rock == "#":
                start = j      
    return res

res = tilt(lines)
print("part1",res)