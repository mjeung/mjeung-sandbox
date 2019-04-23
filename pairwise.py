#!/usr/bin/python

from itertools import combinations 
from subprocess import call  
from os import system, name 
import readchar 
import random

# TODO Features
#
# - Print intructions on each comparison
# - Print progress so the user knows how many more are left
# - Time the amount of time it takes to make a decision
# - Graphical display instead of text
#

# define clear function 
def clear_screen():     
    _ = system('cls')

ls = [
        "Accountability", 
        "Balance", 
        "Belonging", 
        "Collaboration", 
        "Competence", 
        "Contribution", 
        "Cooperations", 
        "Curiousity", 
        "Financial stability", 
        "Growth", 
        "Honesty", 
        "Integrity", 
        "Making a difference", 
        "Reliability", 
        "Resourcefulness", 
        "Stewardship", 
        "Teamwork", 
        "Truth", 
        ]

scorekeeper = {}

for l in ls:
    scorekeeper[l] = 0

comb = combinations(ls, 2)
num_comb = len(list(comb))

clear_screen()
print("")
print("")
print("You will do", num_comb, "comparisons");
print("Estimated time to complete:", num_comb*3, "seconds");
print("")
print("")
print("Press any key to continue or Ctrl+C to quit.")
readchar.readkey();
clear_screen()

comb_ls = list(combinations(ls,2))
random.shuffle(comb_ls)

for c in comb_ls:  
    print(c)
    a = 2
    while a != 'q' and a != 'p':
        a = readchar.readkey();
        print(a);

    if a == 'q':
      scorekeeper[c[0]] += 1;
    else:
      scorekeeper[c[1]] += 1;

    clear_screen()

print(sorted(scorekeeper.items(), key = lambda kv:(kv[1], kv[0])))


