import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input12.txt"
lines = open(str(cur_dir)+file_name).read().splitlines()
    
    
@functools.lru_cache(None)
def dfs(records, index, cgroup, cgroups, cgroupSize):
    cgroups = list(cgroups)
    
    # print(records, index, cgroup, cgroups, cgroupSize)
    global totalLen
    assert cgroups != None
    if any( g1 !=g2 for (g1, g2) in zip(cgroups, cgroupSize)): 
        # print(cgroups, cgroupSize)
        return False
    if  totalLen - sum(cgroups) - len(cgroup) > (len(records) - index + 2) :
        # print(totalLen, len(records), index+2, sum(cgroups), len(cgroup))
        
        return False

    if index == len(records):
        if cgroup != "":
            cgroups.append(len(cgroup))
        # print(all( g1 == g2 for (g1, g2) in zip_longest(cgroups, cgroupSize)))
        # print(cgroups, cgroupSize)
        return all( g1 == g2 for (g1, g2) in zip_longest(cgroups, cgroupSize))
    # pre = records[index-1] if index > 0 else None
    res = 0
    cur = records[index]
    if cur == "?":
        newGroups =  cgroups + [len(cgroup)] if cgroup else cgroups
        #print("111", records, index+1, "", newGroups, cgroupSize)
        res += dfs(records, index+1, "", tuple(newGroups[::]), cgroupSize)
        cgroup += "#"
        #print("222", records, index+1, cgroup, cgroups, cgroupSize)
        res += dfs(records, index+1, cgroup, tuple(cgroups[::]), cgroupSize)
    
    elif cur == ".":
        
        newGroups =  cgroups + [len(cgroup)] if cgroup else cgroups
        #print("333", records, index+1, "", newGroups, cgroups, cgroupSize)
        res += dfs(records, index+1, "", tuple(newGroups[::]), cgroupSize)
    elif cur == "#":
        cgroup += cur
        #print("4444", records, index+1, cgroup, cgroups, cgroupSize)
        res += dfs(records, index+1, cgroup, tuple(cgroups[::]), cgroupSize)
    return res

ans = 0

id = 0
for line in lines:
    id += 1
    print("id: ", id)
    records, cgroupSize = line.split()
    
    cgroupSize_ = cgroupSize
    cgroupSize__ = cgroupSize
    
    base = 5
    cgroupSize = tuple(map(int, cgroupSize.split(",")))
    cgroupSize = cgroupSize * base
    records = "?".join(records for _ in range(base))
    global totalLen 
    totalLen = sum(cgroupSize)
    ans += dfs(records, 0, "", (), cgroupSize)
    
    print(ans)

    
print(ans)    
    
        
        
        
        
        
        
        
    
    