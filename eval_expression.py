#!C:\Python27\bin\python.exe

from sets import Set

#########################################################################
# Overview:
# A friend of mine gave me this problem as a sample interview question.
#
# You are given a string of numbers, such as 12456 and a target number.
#
# You can add + and or * to the string as many times as you like.
# For instance, 12 + 4* 5 * 6 is legal
#
# You must write a function that returns true if it is possible to
# add + and * to the string in order to achieve an expression that
# evaluates to the target number.
#
# For instance, given 12345 and a target of 56, the function would
# return TRUE, because 12 * 3+ 4 * 5 = 56
#
#########################################################################

#
# insert_into_each_possible_position()
#
# INPUT:
# input_string: the string you are manipulating
#               It may already have some non-digits in it
#               legal values: 12345, 1*2345, 1+2+345
#
# insert_character: the character which the function will insert into the
#                   input string
#
# OUTPUT:
# result_strings: a list of strings where the insert_character has been
#                 inserted in each possible possition
#
def insert_into_each_possible_position( input_string, 
                                        insert_character,
                                        result_strings ):
  output_string = "";
  for i in range(len(input_string)):
    if (i!=0) and (i!=len(input_string)):
      if input_string[i].isdigit() and input_string[i-1].isdigit():
        new_string = input_string[:i] + insert_character + input_string[i:]
        result_strings.append(new_string);

#
# recursively_find_all_permutations()
# 
# INPUT:
# input_string: the string you are manipulating
#               It may already have some non-digits in it
#               legal values: 12345, 1*2345, 1+2+345
#
# OUTPUT:
# results: a list of all possible permutations of the input_string
#          
# If the input is 123, the results list is: [1+2], [1*2]
#
def recursively_find_all_permutations(input_string, results):
  subresults = []
  insert_into_each_possible_position( input_string, "*", subresults );
  insert_into_each_possible_position( input_string, "+", subresults );
  if len(subresults) == 0:
    pass
  else:
    for i in subresults:
      results.add(i);
      recursively_find_all_permutations(i, results);

#
# a_permutation_of_this_string_can_evaluate_to_this_target()
#
# INPUT:
# input: the string you are starting with.  Such as "12345"
#
# target: the target value you are testing against.  Such as 56
#
# OUTPUT:
# output: a list that will be populated with the correct expression that
#         evaluates to the target value.  Empty if it is not possible to
#         achieve the target with the given input string
#
# RETURN: True if possible to achieve target, False otherwise
#
def a_permutation_of_this_string_can_evaluate_to_this_target(input, target, output):
  result_set = Set([input])
  recursively_find_all_permutations(input, result_set)
  for r in result_set:
    if eval(r) == target:
      output.append(r);
      return True;
  return False;

#
# Automated unit tests to prove that this works      
#
def run_unit_tests():
  input = "1234"
  result = [] 
  insert_into_each_possible_position(input, "+", result);
  if len(result) != 3: 
    raise Exception('failed test')
  if result[2] != "123+4": 
    raise Exception('failed test')

  input = "12*34"
  result = [] 
  insert_into_each_possible_position(input, "*", result);
  if len(result) != 2: 
    raise Exception('failed test')
  if result[1] != "12*3*4": 
    raise Exception('failed test')

  input = "1+2*3/4"
  result = [] 
  insert_into_each_possible_position(input, "+", result);
  if len(result) != 0: 
    raise Exception('failed test')

  input = "123"
  result_set = Set([])
  recursively_find_all_permutations(input, result_set);
  if len(result_set) != 8: 
    raise Exception('failed test')

  input = "123"
  output = []
  if not a_permutation_of_this_string_can_evaluate_to_this_target(input, 6, output):
    raise Exception('failed test') 

  input = "12345"
  output = []
  if not a_permutation_of_this_string_can_evaluate_to_this_target(input, 357, output):
    raise Exception('failed test') 
  else: 
    print output

  input = "12345"
  output = []
  if not a_permutation_of_this_string_can_evaluate_to_this_target(input, 60, output):
    raise Exception('failed test') 
  else: 
    print output

  input = "12345"
  output = []
  if not a_permutation_of_this_string_can_evaluate_to_this_target(input, 25, output):
    raise Exception('failed test') 
  else: 
    print output

  input = "12345"
  output = []
  if not a_permutation_of_this_string_can_evaluate_to_this_target(input, 81, output):
    raise Exception('failed test') 
  else: 
    print output

  # 2* 2 + 3 * 4
  input = "22345"
  output = []
  if not a_permutation_of_this_string_can_evaluate_to_this_target(input, 28, output):
    raise Exception('failed test') 
  else: 
    print output

  # 12 * 3+ 4 * 5
  input = "12345"
  output = []
  if not a_permutation_of_this_string_can_evaluate_to_this_target(input, 56, output):
    raise Exception('failed test') 
  else: 
    print output

  # 12 * 34 + 5 * 6
  input = "123456"
  output = []
  if not a_permutation_of_this_string_can_evaluate_to_this_target(input, 438, output):
    raise Exception('failed test') 
  else: 
    print output

  # 12 * 34 + 5 * 6
  input = "123456"
  output = []
  if not a_permutation_of_this_string_can_evaluate_to_this_target(input, 123456, output):
    raise Exception('failed test') 
  else: 
    print output

  print ""
  print "Congratulations, all the unit tests passed!"


run_unit_tests();

