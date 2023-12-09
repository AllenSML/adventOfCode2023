import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input09.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

res = 0
for line in lines:
    line = list(map(int, line.split()))    
    prepend = [line[0]]
    while any( n != 0 for n in line):
        newLine = list()
        for i in range(len(line)-1):
            newLine.append(line[i+1] - line[i])
        prepend.append(newLine[0])
        line = newLine
    start = 0
    for n in prepend[::-1]:
        start = n - start
    res += start
    
print("part2: ", res)   

