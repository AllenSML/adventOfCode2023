import os,math, difflib, pathlib, string, re, json, functools, networkx as ntx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input20.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

# ff: state: 
    # on -> off/low, off -> on/hi
    # input can only be low
    
# conj 
    # remmber all connected input as low
    # if all are hi -> low
    # else -> hi
    # first update then check and send 
    
# button module
    # always send -> low
    
# module = {
#     # "xzy": {"state": {}, "mtype": "", "output": []}
#     "xzy": {{}/"off"/"on", "mtype", []}
# }

module = {}
broadcaster = []
for line in lines:
    first, output = line.split(" -> ")    
    outputs = output.split(", ")
    mtype = first[0]
    mname = first[1:].strip()
    #bc
    if first  == "broadcaster":
        broadcaster = outputs
        continue
    #ff
    if mtype == "%":
       module[mname] = [mtype, "off", outputs]
    #cc
    elif mtype == "&":
       module[mname] = [mtype, {}, outputs]


for mname, (mtype, state, outputs) in module.items():
    for mto in outputs:
        if mto in module and module[mto][0] == "&":
            module[mto][1][mname] = "lo"

lonum = 0
hinum = 0

for _ in range(1000):
    queue = deque([("broadcaster", to, "lo") for to in broadcaster])
    lonum += 1
    while queue:
        
        mfrom, mto, inpulse = queue.popleft()
        if inpulse == "hi":
            hinum += 1
        if inpulse == "lo":
            lonum += 1
        if mto not in module:
            continue
        
        mtype, state, outputs = module[mto]
        print("================================")
        print("mfrom, inpulse, mto => ", mfrom, inpulse, mto )
        # print("mtype, state, outputs => " , mtype, state, outputs)
        
        outpulse = None
        if mtype == "%":
            if inpulse == "lo":
                state = "on" if state == "off" else "off"
                module[mto][1] = state
                outpulse = "hi" if state == "on" else "lo"
            else:
                continue            
        elif mtype == "&":
            state[mfrom] = inpulse
            if all (val == "hi" for val in state.values()):
                outpulse = "lo" 
            else:
                outpulse = "hi"
        else:
            
            assert False
        assert outpulse != None
        
        
        for output in outputs:
            queue.append((mto, output, outpulse))

        # if mto == "a":
            # print("===>", len(queue))
            # exit()
    # print(lonum, hinum, lonum + hinum)
    
    
print("part1: ", lonum, hinum, lonum * hinum)

            
            



