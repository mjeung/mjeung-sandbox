#!/Python27/python.exe
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

for combo in list(itertools.combinations('1345678',5)):
	if digitalRoot(map(int,combo)) == doorNumber:
		print map(int,combo), " go into door ", doorNumber
		remaining = map(int,set(['1','3','4','5','6','7','8']) - set(combo) )
		print remaining, "can go into door ", digitalRoot(remaining)
		print "*******"

