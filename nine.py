#!/usr/bin/python
import itertools

def digitalRoot( numbers ):
	answer = 0
	for number in numbers:
		answer = number + answer

	while (answer > 9):
		number_list = [int(i) for i in str(answer)]
		answer = 0
		for number in number_list:
			answer = number + answer

	return answer;

assert digitalRoot([1,2,3]) == 6
assert digitalRoot([1,2,3,4,5]) == 6
assert digitalRoot([1,2,3,4,5,6,7,8]) == 9

doorNumber = 9
numberOfPeople = 4
people = '1345678'

for combo in list(itertools.combinations(people,numberOfPeople)):
	if digitalRoot(map(int,combo)) == doorNumber:
		print ""
		print "*****************"
		print map(int,combo), " can go into door", doorNumber
		remaining = map(int, set(list(people)) - set(combo) )
                if len(remaining) >= 3:
			print remaining, "can go into door ", digitalRoot(remaining)
		else:
			print remaining, "are stuck" 


print ""
