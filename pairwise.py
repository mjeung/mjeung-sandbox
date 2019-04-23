#!/usr/bin/python

from itertools import combinations 
import readchar 

# TODO Features
#
# - Randomize the presentation of the choices
# - Clear the screen after each comparison
# - Print intructions on each comparison
# - Graphical display instead of text
#

ls = [
        "Dishes", 
        "Laundry", 
        "Garbage",
        "Organize",
        ]

scorekeeper = {}

for l in ls:
    scorekeeper[l] = 0

comb = combinations(ls, 2)
num_comb = len(list(comb))

print("")
print("You will do", num_comb, "comparisons");
print("Estimated time to complete:", num_comb*3, "seconds");
print("")
print("Press any key to continue or Ctrl+C to quit.")
readchar.readkey();

for c in list(combinations(ls,2)):  
    print(c)
    a = 2
    while a != 'q' and a != 'p':
        a = readchar.readkey();
        print(a);

    if a == 'q':
      scorekeeper[c[0]] += 1;
    else:
      scorekeeper[c[1]] += 1;

print(sorted(scorekeeper.items(), key = lambda kv:(kv[1], kv[0])))
