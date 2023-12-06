import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

def calc_time(time, dist):
    ans = 1
    for i in range(len(time)):
        ways = 0
        for t in range(time[i]):
            if (time[i] - t) * t > dist[i]:
                ways += 1
        ans = ans * ways
    return ans

time = [45, 98, 83, 73]
dist = [295, 1734, 1278, 1210]
res = calc_time(time, dist)
print("part1: ", res)

time = [45988373]
dist = [295173412781210]
res = calc_time(time, dist) 
print("part2: ", res)   
