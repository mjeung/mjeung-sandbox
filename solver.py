candidates = {'about',
              'after',
              'again',
              'below',
              'could',
              'every',
              'first',
              'found',
              'great',
              'house',
              'large',
              'learn',
              'never',
              'other',
              'place',
              'plant',
              'point',
              'right',
              'small',
              'sound',
              'spell',
              'still',
              'study',
              'their',
              'there',
              'these',
              'thing',
              'think',
              'three',
              'water',
              'where',
              'which',
              'world',
              'would',
              'write',
							}

list0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

s = input()
list1 = s.split(" ")

master_list=[ list0, list1, list2, list3, list4]

temp_candidates = candidates.copy();

for possible_solution in candidates:
	index = 0
	for possible_letter in possible_solution:
		if possible_letter not in master_list[index]:
			if possible_solution in temp_candidates:
				temp_candidates.remove(possible_solution) 
		index+=1

print(temp_candidates)

s = input()
list2 = s.split(" ")

master_list=[ list0, list1, list2, list3, list4]

temp_candidates = candidates.copy();

for possible_solution in candidates:
	index = 0
	for possible_letter in possible_solution:
		if possible_letter not in master_list[index]:
			if possible_solution in temp_candidates:
				temp_candidates.remove(possible_solution) 
		index+=1

print(temp_candidates)

s = input()
list3 = s.split(" ")

master_list=[ list0, list1, list2, list3, list4]

temp_candidates = candidates.copy();

for possible_solution in candidates:
	index = 0
	for possible_letter in possible_solution:
		if possible_letter not in master_list[index]:
			if possible_solution in temp_candidates:
				temp_candidates.remove(possible_solution) 
		index+=1

print(temp_candidates)
