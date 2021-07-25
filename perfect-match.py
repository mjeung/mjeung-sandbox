#function foo()
#{
#  create SET of N.  (Example: N=4, set looks like [1,2,3,4])
#
#  for i: 1..N
#  {
#    selected_number = randomly take number from the SET
#    remove selected_number from SET
#
#    if (i == selected_number)  # we consider this a "perfect match"
#      record_a_failure()
#      set(failure_flag)
#      break
#  }  
#
#  if !failure_flag
#    record_a_success()
#}

#Run function foo() 3-zillion times and then output success / 3-zillion

import random

success_counter = 0
fail_counter = 0

def run_trial():
  global success_counter
  global fail_counter
  failure_flag = 0
  my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

  for x in range(1, 11):
    #print(my_set)
    element = random.sample(my_set, 1)[0]
    my_set.remove(element)
    #print("we're on", x)

    if (x == element):
      #print("we failed!")
      fail_counter = fail_counter + 1
      failure_flag = 1
      break

  if (failure_flag == 0):
    success_counter = success_counter + 1


for trial in range(0,1000000):
  run_trial()

print("total trials:", success_counter + fail_counter)
print("successes:", success_counter)
print("failures:", fail_counter)
print("rate:", success_counter / (success_counter + fail_counter))
