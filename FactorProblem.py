#!/usr/bin/python

import string
import itertools

class FewestFactors(object):
  def __init__(self):
    print "Constructed";

  def number(self,l):
    bestFactors = int(9999999);
    bestValue = int(-9999999);

    allPermutations = self.permutations(l);
    for listCandidate in allPermutations:
      intCandidate = self.convertListToInt(listCandidate)
      numFactors = self.numberOfFactors(intCandidate) 
      if numFactors < bestFactors:
        bestValue = intCandidate
        bestFactors = numFactors
      elif numFactors == bestFactors:
        if intCandidate < bestValue:
          bestValue = intCandidate
    return bestValue;

  # Given list of digits
  # return list of numbers for all possible digit permutations
  def permutations(self,l):
    return list(itertools.permutations(l))

  # Given number, return number of factors
  def numberOfFactors(self,num):
    counter = 0;
    for n in range(1,num+1):
      if num % n == 0:
        counter = counter + 1;
    return counter;

  # Given list of digits, return corresponding int value
  def convertListToInt(self,l):
    s = map(str, l)
    s = ''.join(s)
    s = int(s)
    return s;

ff = FewestFactors()

## TESTS ###
a = [1,2];
ret = ff.permutations(a);
if len(ret) != 2: raise AssertionError
if ff.number(a) != 21: raise AssertionError

if ff.numberOfFactors(7) != 2: raise AssertionError
if ff.numberOfFactors(13) != 2: raise AssertionError
if ff.numberOfFactors(4) != 3: raise AssertionError
if ff.numberOfFactors(10) != 4: raise AssertionError

if ff.convertListToInt([1,2,3]) != 123: raise AssertionError
if ff.convertListToInt([9,5,3]) != 953: raise AssertionError
if ff.convertListToInt([5,5,5]) != 555: raise AssertionError
if ff.convertListToInt([0,5,5]) != 55: raise AssertionError

if ff.number([1,2]) != 21: raise AssertionError
if ff.number([6,0]) != 6: raise AssertionError
if ff.number([4,7,4]) != 447: raise AssertionError
if ff.number([1,3,7,9]) != 1973: raise AssertionError
if ff.number([7,5,4,3,6]) != 36457: raise AssertionError
if ff.number([4,2,1]) != 241: raise AssertionError
if ff.number([2,4,1]) != 241: raise AssertionError
