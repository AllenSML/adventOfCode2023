import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input01.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")


ans = 0

for x in lines:
    digits = [c for c in x if c.isdigit()]
    ans += int(digits[0] + digits[-1])

print("part1:", ans)



ans = 0
digits = "one two three four five six seven eight nine".split()

d2n = dict((digit, str(i)) for digit, i in zip(digits, range(1,10)))
regExp = "(?=(" + "|".join(digits) + "|\\d))"

def help(x):
    if x in d2n:
        return d2n[x]
    return x

for line in lines:
    digits = [*map(help, re.findall(regExp, line))]
    ans += int(digits[0] + digits[-1])

print("part2:", ans)