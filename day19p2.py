import os,math, difflib, pathlib, string, re, json, functools, networkx as ntx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input19.txt"
sections = open(str(cur_dir)+file_name).read().split("\n\n")

lines = sections[0].splitlines()
parts = sections[1].splitlines()

ws = {}
for line in lines:     
    name, rules = line[:-1].split("{")
    rules = rules.split(",")
    ws[name] = ([], rules[-1])    
    for rule in rules[:-1]:
        cond, target = rule.split(":")
        ws[name][0].append((cond[0], cond[1], cond[2:], target))

ops = {
    ">": lambda x,y: x > y,
    "<": lambda x,y: x < y,
}


def help(part, name="in"):
    if name == "R":
        return False
    if name == "A":
        return True
    rules, default = ws[name]
    for key, comparator, value, nextws in rules:
        if ops[comparator](part[key], int(value)):
            return help(part, nextws)
    return help(part, default)        

ans = 0
for part in parts:
    rates = part[1:-1].split(",")
    item = {}
    for rate in rates:
        key, val = rate.split("=")
        item[key] = int(val)
    if help(item):
        ans += sum(item.values())
        
print("part1: ", ans)        