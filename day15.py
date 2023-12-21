import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input15.txt"
steps = open(str(cur_dir)+file_name).read().replace('\n', '').split(',')

sum = 0
for step in steps:
    current = 0
    for ch in step:
        current += ord(ch) 
        current = (current * 17) % 256
    sum += current    

print("part1: ", sum)