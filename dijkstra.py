#!/usr/bin/python


class Edge(object):
   def __init__(self, src, dst, cost):
      self.src = src
      self.dst = dst
      self.cost = cost

class Vertex(object):
   def __init__(self, name):
      self.name = name
      self.visited = False
      self.best_src = "NAN" 
      self.best_cost = 99 
      self.path_to_neighbor = []
   def addEdge(self, destination, cost):
      self.path_to_neighbor.append( Edge(self, destination, cost) )
   def getNeighborEdges(self):
      return self.path_to_neighbor;

a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")

a.addEdge(b,9)
a.addEdge(c,2)

b.addEdge(a,2)
b.addEdge(c,4)
b.addEdge(d,2)

c.addEdge(a,9)
c.addEdge(b,4)
c.addEdge(d,3)

d.addEdge(c,3)
d.addEdge(b,2)

graph = { a.name: a,
          b.name: b,
          c.name: c,
          d.name: d }

# find fastest path between A and D

# This function takes a vertices V
# For each adjacent vertices (AV) that haven't been visited yet
# If the cost to get to AV is LESS THAN AV's currently recorded best cost
#   overwrite AV's best cost, best src
# Mark vertice V visited
# next vertice we visit MUST be the lowest cost...

for k, v in graph.items():
  if (v.visited == True):
    continue
  else:
    neighborEdges = v.getNeighborEdges();
    for edge in neighborEdges:
      if (edge.dst.best_cost > edge.cost):
        edge.dst.best_cost = edge.cost + v.best_cost
        edge.dst.bast
