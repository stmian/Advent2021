# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 04:17:44 2021

@author: Sami
"""

from collections import Counter


def solve(pairs, tmpl, steps):
    for step in range(steps + 1):
        # count all letters
        if step == steps:
            letters = Counter()
            for pair in pairs:
                letters[pair[0]] += pairs[pair]
            letters[tmpl[-1]] += 1
            return max(letters.values()) - min(letters.values())
        # add all new pairs
        new_pairs = Counter()
        for pair in pairs:
            new_pairs[pair[0] + rules[pair]] += pairs[pair]
            new_pairs[rules[pair] + pair[1]] += pairs[pair]
        pairs = new_pairs


data = open("input.txt").read().strip().split("\n\n")
# keep track of pair count
tmpl = data[0]
pairs = Counter()
for i in range(len(tmpl) - 1):
    pairs[tmpl[i] + tmpl[i + 1]] += 1
# setup dict of rules for easy lookup
rules = {}
for line in data[1].split("\n"):
    pair, elem = line.split(" -> ")
    rules[pair] = elem
# solve parts
print(f"Part 1: {solve(pairs, tmpl, 10)}")
print(f"Part 2: {solve(pairs, tmpl, 40)}")