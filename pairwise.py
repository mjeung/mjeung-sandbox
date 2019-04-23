#!/usr/bin/python

from itertools import combinations 
import readchar 

list = [
        "Accountability", 
        "Achievement", 
        "Adaptability",
        "Adventure",
        "Altruism",
        "Ambition",
        "Authenticity",
        "Balance"
        ]


scorekeeper = {}

for l in list:
    scorekeeper[l] = 0

comb = combinations(list, 2)

for c in comb:  
    print(c)
    a = 2
    while a != 'q' and a != 'p':
        a = readchar.readkey();
        print(a);

    if a == 'q':
      scorekeeper[c[0]] += 1;
    else:
      scorekeeper[c[1]] += 1;

print(scorekeeper)

print(sorted(scorekeeper.items(), key = lambda kv:(kv[1], kv[0])))
