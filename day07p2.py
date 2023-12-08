import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input07.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

cards = list('AKQJT98765432J')
weights = dict((c, i ) for c, i in zip(cards, range(13, -1, -1)))

hands = list()
for line in lines:
    hand, bid = line.split()
    bid = int(bid)
    
    weight = sum(weights[c] * (14**(4-i)) for i, c in enumerate(hand))
    
    kind = 0
    jCnt = hand.count("J")
    hand_ = hand.replace("J", "")
    
    for index, x in enumerate(Counter(hand_).most_common(2)):
        cnt = x[1] + (jCnt if index == 0 else 0)
        if cnt == 5:
            kind += 10
        elif cnt == 4:
            kind += 8
        elif cnt == 3:
            kind += 5
        elif cnt == 2:
            kind += 2
    
    if not hand_:
        kind = 10
        
    kind = kind * 1000000
    hands.append((kind + weight, bid, hand)) 
    
hands.sort()

res = 0
for i,r in enumerate(hands):
    res += (i+1) * r[1]
    
print(res)
