import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input18.txt"
input = open(str(cur_dir)+file_name).read()
plans = [line.split() for line in input.split("\n")]

diMap = {"U":(0,-1),"D":(0,1),"R":(1,0),"L":(-1,0)}
num2Di = "RDLU"

grid = list()
pos = [0,0]

def convertHexaToDecimal(hexa):    
    hexa = hexa[1:-1]
    return int(hexa, 16)

idx = 0
totalLen = 0
for _, __, colour in plans:
    idx += 1
    colour = colour[1:-1]    
    distance = convertHexaToDecimal(colour)
    di = num2Di[int(colour[-1])]    
    pos[0] += diMap[di][0] * distance
    pos[1] += diMap[di][1] * distance
    grid.append(tuple(pos))
    totalLen += distance

total = 0    
for i in range(len(grid)):
    total += grid[i][0] * (grid[i-1][1] - grid[(i+1)%len(grid)][1])

total = abs(total) // 2

print(total + totalLen // 2 + 1)