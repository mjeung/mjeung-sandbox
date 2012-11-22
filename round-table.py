#!/usr/bin/python

class Employee(object):
  def __init__(self, company, id):
    self.myCompany = company
    self.myId = id

  def display(self):
    print self.myCompany, "employee, id: ", self.myId

  myCompany = ""
  myId = 0

##################################################
class EmployeeGenerator(object):
  def makeEmployee(self, company):
    self.counter = self.counter + 1
    return Employee(company,self.counter)

  counter = 0
  

##################################################

class RoundTable(object):

  def arrangements(self, countA, countB, chairs, minDistance):
    print "countA: ", countA
    print "countB: ", countA
    print "chairs: ", chairs
    print "minDistance: ", minDistance

    # Build Table
    for i in range(0,chairs):
      self.table.append(0)

    # Build list of employees
    for i in range(0,countA):
      self.listOfEmployees.append(employeeGenerator.makeEmployee("Phoenix"))
    for i in range(0,countB):
      self.listOfEmployees.append(employeeGenerator.makeEmployee("Corsair"))

    print self.table

    return 10;

  table = []
  listOfEmployees = []
  employeeGenerator = EmployeeGenerator()

#  def recursiveFindSolution(table): 


countA = 1
countB = 1
chairs = 10
minDistance = 1
roundTable = RoundTable()
returnValue = roundTable.arrangements(countA, countB, chairs, minDistance);
 
print "returnValue: ", returnValue

