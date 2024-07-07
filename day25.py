import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product, zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy


cur_dir = pathlib.Path(__file__).resolve().parents[0]
file_name ="/input25.txt"
input = open(str(cur_dir)+file_name).read().split("\n")

g = nx.Graph()

for line in input:
    left, right = line.split(":")
    for node in right.strip().split():
        g.add_edge(left, node)
        g.add_edge(node, left)

g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a) * len(b))