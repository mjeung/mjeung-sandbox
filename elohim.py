import sys
import copy
import cProfile
from random import shuffle


class Shape(object):
  def __init__(self):
    self.id = 0
    self.Matrix = [[0]*5 for i in range(4)]
    self.do_not_rotate = False
    self.rotate_only_once = False

  def display(self):
    for row in range(4):
      for col in range(4):
        if self.Matrix[row][col] == 0:
          sys.stdout.write(' ');
        else:
          sys.stdout.write(str(self.Matrix[row][col]));
      sys.stdout.write('\n');

  def has_empty_space_on_left(self):
    if self.Matrix[0][0] == 0:
      if self.Matrix[1][0] == 0:
        if self.Matrix[2][0] == 0:
          if self.Matrix[3][0] == 0:
            return True
    return False

  def has_empty_space_on_top(self):
    if self.Matrix[0][1] == 0:
      if self.Matrix[0][2] == 0:
        if self.Matrix[0][3] == 0:
          if self.Matrix[0][4] == 0:
            return True
    return False

  def init_as_line(self,id):
    self.id = id
    self.Matrix = [[0]*5 for i in range(4)]
    self.Matrix[0][0] = id
    self.Matrix[0][1] = id
    self.Matrix[0][2] = id
    self.Matrix[0][3] = id
    self.rotate_only_once = True

  def init_as_l_shape(self,id):
    self.id = id
    self.Matrix = [[0]*5 for i in range(4)]
    self.Matrix[0][0] = id
    self.Matrix[1][0] = id
    self.Matrix[2][0] = id
    self.Matrix[2][1] = id

  def init_as_j_shape(self,id):
    self.id = id
    self.Matrix = [[0]*5 for i in range(4)]
    self.Matrix[0][1] = id
    self.Matrix[1][1] = id
    self.Matrix[2][0] = id
    self.Matrix[2][1] = id

  def init_as_e_shape(self,id):
    self.id = id
    self.Matrix = [[0]*5 for i in range(4)]
    self.Matrix[0][0] = id
    self.Matrix[1][0] = id
    self.Matrix[1][1] = id
    self.Matrix[2][0] = id

  def init_as_2_shape(self,id):
    self.id = id
    self.Matrix = [[0]*5 for i in range(4)]
    self.Matrix[0][1] = id
    self.Matrix[1][0] = id
    self.Matrix[1][1] = id
    self.Matrix[2][0] = id
    self.rotate_only_once = True

  def init_as_5_shape(self,id):
    self.id = id
    self.Matrix = [[0]*5 for i in range(4)]
    self.Matrix[0][0] = id
    self.Matrix[1][0] = id
    self.Matrix[1][1] = id
    self.Matrix[2][1] = id
    self.rotate_only_once = True

  def init_as_box(self,id):
    self.id = id
    self.Matrix = [[0]*5 for i in range(4)]
    self.Matrix[0][0] = id
    self.Matrix[1][0] = id
    self.Matrix[1][1] = id
    self.Matrix[0][1] = id
    self.do_not_rotate = True

  def rotate_clockwise(self, shift_top_left):
    tmpMatrix = [[0]*5 for i in range(4)]
    for y in range(4):
      for x in range(4):
        tmpMatrix[x][3-y] = self.Matrix[y][x]

    for y in range(4):
      for x in range(4):
        self.Matrix[x][y] = tmpMatrix[x][y]

    if shift_top_left:
      while self.has_empty_space_on_top() == True:
        self.slide_up_one()
      while self.has_empty_space_on_left() == True:
        self.slide_left_one()

  def slide_up_one(self):
    for col in range(4): 
      for row in range(4): 
	if row != 3:
          self.Matrix[row][col] = self.Matrix[row+1][col]
        else:
          self.Matrix[row][col] = 0

  def slide_left_one(self):
    for row in range(4): 
      for col in range(4): 
	if col != 3:
          self.Matrix[row][col] = self.Matrix[row][col+1]
        else:
          self.Matrix[row][col] = 0

class Grid(object):
  def __init__(self,row,col):
    self.max_row = row
    self.max_col = col
    self.Matrix = [[0]*(col+1) for i in range(row)]

  def open_row(self):
    for row in range(self.max_row):
      for col in range(self.max_col):
        if (self.Matrix[row][col] == 0):
          return row

  def open_col(self):
    for row in range(self.max_row):
      for col in range(self.max_col):
        if (self.Matrix[row][col] == 0):
          return col

  def display(self):
    for row in range(self.max_row):
      for col in range(self.max_col):
        if (self.Matrix[row][col] == 0):
          sys.stdout.write('.');
	else:
          sys.stdout.write(str(unichr(int(self.Matrix[row][col])+96)));
      sys.stdout.write('\n');

  def place(self,shape,row_position,col_position):
#    print "max_row", self.max_row
#    print "max_col", self.max_col
    placed_blocks_count = 0
    for row in range(4):
      for col in range(4):
        if row + row_position < self.max_row:
          if col + col_position < (self.max_col):
#            print "row", row
#            print "row_position", row_position
#            print "col", col
#            print "col_position", col_position
#            print "col + col_position", col + col_position
#            print "row + row_position", row + row_position

	    if (shape.Matrix[row][col] != 0):
	      if (self.Matrix[row+row_position][col+col_position] == 0):
                placed_blocks_count = placed_blocks_count + 1
                self.Matrix[row + row_position][col + col_position] = shape.Matrix[row][col]
#                self.display()

    if placed_blocks_count != 4:
      #print "Placement isn't Good Because not Enough Blocks Placed"
      return False
    else:
      if self.top_left_corner_is_ok():
        for row in range(self.max_row):
          for col in range(self.max_col):
            node = (row,col)
            filled_nodes = self.flood_fill(node, 0, -1)
            #print "filled_nodes", filled_nodes
            if filled_nodes % 4 != 0:
              #print "Placement isn't Good, Too Small Hole Exists"
              return False
             
        #print "Placement GOOD!"
        return True
        #if self.no_1x1_holes():
        #  return True
      else:
        #print "Placement isn't GOOD because of topleftcorner check"
        return False 

  def is_finished(self):
    for row in range(self.max_row):
      for col in range(self.max_col):
        if self.Matrix[row][col] == 0:
          return False
    return True

  def no_1x1_holes(self):

    for row in range(self.max_row):
      for col in range(self.max_col):

        check_above = True
        check_below = True
        check_left = True
        check_right = True

        if self.Matrix[row][col] == 0:
          if (row + 1 >= self.max_row):
            check_below = False
          if (row - 1 < 0):
            check_above = False
          if (col + 1 >= self.max_col):
            check_right = False
          if (col - 1 < 0):
            check_left = False

          adjacency_count = 0
          if not check_above:
            adjacency_count = adjacency_count + 1
          elif self.Matrix[row-1][col] != 0:
            adjacency_count = adjacency_count + 1

          if not check_below:
            adjacency_count = adjacency_count + 1
          elif self.Matrix[row+1][col] != 0:
            adjacency_count = adjacency_count + 1

          if not check_left:
            adjacency_count = adjacency_count + 1
          elif self.Matrix[row][col-1] != 0:
            adjacency_count = adjacency_count + 1
 
          if not check_right:
            adjacency_count = adjacency_count + 1
          elif self.Matrix[row][col+1] != 0:
            adjacency_count = adjacency_count + 1

          if adjacency_count > 3:
            return False

    return True
       

# Algorithm Taken from Wikipedia
# http://en.wikipedia.org/wiki/Flood_fill
#
# Flood-fill (node, target-color, replacement-color):
#  1. Set Q to the empty queue.
#  2. If the color of node is not equal to target-color, return.
#  3. Add node to Q.
#  4. For each element N of Q:
#  5.         Set w and e equal to N.
#  6.         Move w to the west until the color of the node to the west of w no longer matches target-color.
#  7.         Move e to the east until the color of the node to the east of e no longer matches target-color.
#  8.         For each node n between w and e:
#  9.             Set the color of n to replacement-color.
# 10.             If the color of the node to the north of n is target-color, add that node to Q.
# 11.             If the color of the node to the south of n is target-color, add that node to Q.
# 12. Continue looping until Q is exhausted.
# 13. Return.

  def flood_fill(self, node, target_number, replacement_number):

    if ( self.Matrix[node[0]][node[1]] != target_number):
      return 4
 
    q = []
    q.append(node)
    number_of_filled_nodes = 0

    for n in q:
      west = (n[0],n[1]);
      east = (n[0],n[1]);

#      print "east current:", east[0], east[1]
      while east[1] + 1 < self.max_col and self.Matrix[east[0]][east[1] + 1] == target_number:
#        print "searching east"
        east = (east[0], east[1]+1)
#        print east[0], east[1]+1, self.max_row
#        if east[1]+1 >= self.max_row:  # boundary check
#          print "east nope!"
#          break

#      print "west current: ", west[0], west[1]
      while west[1] > 0 and self.Matrix[west[0]][west[1] - 1] == target_number:
#        print "searching west"
        west = (west[0],west[1]-1)
#        print west[0], west[1]-1, self.max_row
#        if west[1]-1 < 0:  # boundary check
##          print "west nope!"
#          break

      counter = west[1]
      fill_node = (west[0],west[1])
      while counter <= east[1]:
#        print counter
        if self.Matrix[fill_node[0]][fill_node[1]] != replacement_number:
          self.Matrix[fill_node[0]][fill_node[1]] = replacement_number
          number_of_filled_nodes = number_of_filled_nodes + 1
#        print number_of_filled_nodes
#        self.display()
        counter = counter + 1
        if fill_node[0] - 1 >= 0:
          if self.Matrix[fill_node[0]-1][fill_node[1]] == target_number:
            north_node = (fill_node[0]-1, fill_node[1])
            q.append(north_node)
        if fill_node[0] + 1 < self.max_row:
          if self.Matrix[fill_node[0]+1][fill_node[1]] == target_number:
            south_node = (fill_node[0]+1, fill_node[1])
            q.append(south_node)

        fill_node = (fill_node[0],counter)

#    self.display()
#    print "number_of_filled_nodes1: ", number_of_filled_nodes

    if replacement_number != 0:
      self.flood_fill(node,replacement_number,target_number)

#    print "number_of_filled_nodes2: ", number_of_filled_nodes
    return number_of_filled_nodes


  def top_left_corner_is_ok(self):
    if self.max_row >= 3:
      if self.max_col >= 3:

        # Recognize this situation:
        #
        #   +----
        #   |.j..
        #   |.j..
        #   |jj..
        #   |....
        #
        if self.Matrix[0][0] == 0:
          if self.Matrix[1][0] == 0:
            if self.Matrix[0][1] != 0:
              if self.Matrix[1][1] != 0:
                if self.Matrix[2][0] != 0:
                  return False

        # Recognize this situation:
        #
        #   +----
        #   |..l.
        #   |lll.
        #   |....
        #   |....
        #
        if self.Matrix[0][0] == 0:
          if self.Matrix[0][1] == 0:
            if self.Matrix[1][0] != 0:
              if self.Matrix[1][1] != 0:
                if self.Matrix[0][2] != 0:
                  return False

        # Recognize this situation:
        #
        #   +----
        #   |.x..
        #   |xx..
        #   |....
        #   |....
        #
        if self.Matrix[0][0] == 0:
          if self.Matrix[1][0] != 0:
            if self.Matrix[0][1] != 0:
              return False

        # Recognize this situation:
        #
        #   +---------+
        #   |.......x.|
        #   |.......xx|
        #   |.........|
        #   |.........|
        #
        if self.Matrix[0][self.max_col - 1] == 0:
          if self.Matrix[0][self.max_col - 2] != 0:
            if self.Matrix[1][self.max_col - 1] != 0:
              return False

        # Recognize this situation:
        #
        #   +---------+
        #   |......x..|
        #   |.......xx|
        #   |.........|
        #   |.........|
        #
        if self.Matrix[0][self.max_col - 1] == 0:
          if self.Matrix[0][self.max_col - 2] == 0:
            if self.Matrix[0][self.max_col - 3] != 0:
              if self.Matrix[1][self.max_col - 1] != 0:
                if self.Matrix[1][self.max_col - 2] != 0:
                  return False

        # Recognize this situation:
        #
        #   +---------+
        #   |......x..|
        #   |......x.x|
        #   |.......x.|
        #   |.........|
        #
        if self.Matrix[0][self.max_col - 1] == 0:
          if self.Matrix[0][self.max_col - 2] == 0:
            if self.Matrix[1][self.max_col - 2] == 0:
              if self.Matrix[0][self.max_col - 3] != 0:
                if self.Matrix[1][self.max_col - 3] != 0:
                  if self.Matrix[2][self.max_col - 2] != 0:
                    if self.Matrix[1][self.max_col - 1] != 0:
                      return False

        # Recognize this situation:
        #
        #   +---------+
        #   |.....x...|
        #   |......xxx|
        #   |.........|
        #   |.........|
        #
        if self.Matrix[0][self.max_col - 1] == 0:
          if self.Matrix[0][self.max_col - 2] == 0:
            if self.Matrix[0][self.max_col - 3] == 0:
              if self.Matrix[0][self.max_col - 4] != 0:
                if self.Matrix[1][self.max_col - 1] != 0:
                  if self.Matrix[1][self.max_col - 2] != 0:
                    if self.Matrix[1][self.max_col - 3] != 0:
                      return False

    return True

def number_of_open_adjacencies(grid,row,col):

  open_adjacencies = 0;

  check_above = True
  check_below = True
  check_left = True
  check_right = True

  if grid.Matrix[row][col] == 0:
    if (row + 1 >= grid.max_row):
      check_below = False
    if (row - 1 < 0):
      check_above = False
    if (col + 1 >= grid.max_col):
      check_right = False
    if (col - 1 < 0):
      check_left = False

  if check_above and grid.Matrix[row-1][col] == 0:
    open_adjacencies = open_adjacencies + 1;

  if check_below and grid.Matrix[row+1][col] == 0:
    open_adjacencies = open_adjacencies + 1;

  if check_left and grid.Matrix[row][col-1] == 0:
    open_adjacencies = open_adjacencies + 1;

  if check_right and grid.Matrix[row][col+1] == 0:
    open_adjacencies = open_adjacencies + 1;

  return open_adjacencies

# rapidly identify impossible to fill holes within the grid
def grid_is_impossible(grid):
  for row in range(grid.max_row):
    for col in range(grid.max_col):
      if grid.Matrix[row][col] == 0:
        # this is potentially a hole
        copy1 = copy.deepcopy(grid)

        copy1.Matrix[row][col] = 9  # fill in this spot
        size_of_hole = 1

        check_above = True
        check_below = True
        check_left = True
        check_right = True

        if grid.Matrix[row][col] == 0:
          if (row + 1 >= grid.max_row):
            check_below = False
          if (row - 1 < 0):
            check_above = False
          if (col + 1 >= grid.max_col):
            check_right = False
          if (col - 1 < 0):
            check_left = False

        size_of_hole = 1
        if check_above: 
          size_of_hole += number_of_open_adjacencies(copy1,row-1,col)
        if check_below: 
          size_of_hole += number_of_open_adjacencies(copy1,row+1,col)
        if check_left: 
          size_of_hole += number_of_open_adjacencies(copy1,row,col+1)
        if check_right: 
          size_of_hole += number_of_open_adjacencies(copy1,row,col-1)

        if size_of_hole < 2:
          return False;
        else:
          return True
      
       

    


def test_is_finished1():
  shape = Shape();
  shape.init_as_box(1)

  grid = Grid(2,2);
  grid.place(shape,0,0);

  if (False == grid.is_finished()):
    print "FAIL1"

def test_is_finished2():
  shape = Shape();
  shape.init_as_box(1)

  grid = Grid(2,3);
  grid.place(shape,0,0);

  grid.display()

  if (True == grid.is_finished()):
    print "FAIL2"

def test_has_empty_space_on_left():
  shape = Shape();
  shape.init_as_box(1)
  if shape.has_empty_space_on_left():
    print "FAIL3"
  shape.rotate_clockwise(False)
  if shape.has_empty_space_on_left() == False:
    print "FAIL4"

def test_has_empty_space_on_top():
  shape = Shape();
  shape.init_as_box(1)
  if shape.has_empty_space_on_top():
    print "FAIL5"
  shape.rotate_clockwise(False)
  shape.rotate_clockwise(False)
  if shape.has_empty_space_on_top() == False:
    print "FAIL!"

def test_rotate_and_slide_top_left():
  shape = Shape();
  shape.init_as_box(1)
  if shape.has_empty_space_on_top():
    print "FAIL!"
  if shape.has_empty_space_on_left():
    print "FAIL!"
  shape.rotate_clockwise(True)
  if shape.has_empty_space_on_top():
    print "FAIL!"
  if shape.has_empty_space_on_left():
    print "FAIL!"
  shape.rotate_clockwise(True)
  if shape.has_empty_space_on_top():
    print "FAIL!"
  if shape.has_empty_space_on_left():
    print "FAIL!"
  shape.rotate_clockwise(True)
  if shape.has_empty_space_on_top():
    print "FAIL!"
  if shape.has_empty_space_on_left():
    print "FAIL!"

def test_impossible_to_place():
  shape = Shape();
  shape.init_as_line(1)
  grid = Grid(2,2);
  if (grid.place(shape,0,0) == True ):
    print "Fail!"
  shape.rotate_clockwise(True)
  if (grid.place(shape,0,0) == True ):
    print "Fail!"
  shape.rotate_clockwise(True)
  if (grid.place(shape,0,0) == True ):
    print "Fail!"
  shape.rotate_clockwise(True)
  if (grid.place(shape,0,0) == True ):
    print "Fail!"

def test_regular_place():
  grid = Grid(2,4)
  s1 = Shape()
  s1.init_as_l_shape(1)
  s2 = Shape()
  s2.init_as_l_shape(2)

  s1.rotate_clockwise(True)
  s2.rotate_clockwise(True)
  s2.rotate_clockwise(True)
  s2.rotate_clockwise(True)
  grid.place(s1,0,0)
  grid.place(s2,0,1)
  if (not grid.is_finished()):
    print "FAIL"

def test_recursive_place1():
  grid = Grid(2,4)
  s1 = Shape()
  s1.init_as_l_shape(1)
  s2 = Shape()
  s2.init_as_l_shape(2)

  mylist = [s1, s2]
  recursive_solve(grid, mylist)

def test_recursive_place2():
  grid = Grid(4,4)
  s1 = Shape()
  s1.init_as_l_shape(1)
  s2 = Shape()
  s2.init_as_j_shape(2)
  s3 = Shape()
  s3.init_as_box(3)
  s4 = Shape()
  s4.init_as_line(4)

  mylist = [s1, s2, s3, s4]
  recursive_solve(grid, mylist)

def test_recursive_place3():
  grid = Grid(4,8)
  s1 = Shape()
  s1.init_as_l_shape(1)
  s2 = Shape()
  s2.init_as_j_shape(2)
  s3 = Shape()
  s3.init_as_box(3)
  s4 = Shape()
  s4.init_as_line(4)

  s5 = Shape()
  s5.init_as_l_shape(5)
  s6 = Shape()
  s6.init_as_j_shape(6)
  s7 = Shape()
  s7.init_as_box(7)
  s8 = Shape()
  s8.init_as_line(8)

  mylist = [s2, s1, s3, s5, s7, s4, s8, s6]
  recursive_solve(grid, mylist)


# this describes the recursive function that will solve the problem
#
# If there are more pieces in the list,
#  Make a copy of Grid
#   Select a piece from the list (remove it)
#   Attempt to Place it in x,y location
#     On succcess, call this function again!
#     On Fail:  Rotate 1 time
#       Attempt to Place it in x,y location
#       On succcess, call this function again!
#         On Fail:  Rotate 1 time
#         Attempt to Place it in x,y location
#         On succcess, call this function again!
#           On Fail:  Rotate 1 time
#           Attempt to Place it in x,y location
#           On succcess, call this function again!
# Base Case
#  -- All pieces are placed
#
def recursive_solve(grid,list_of_remaining_shapes):
#  print len( list_of_remaining_shapes)
  print ""
  grid.display()

  if not list_of_remaining_shapes:  #check of empty
    if grid.is_finished():
      print ""
      print "My solution:"
      grid.display()
      sys.exit(0) 
    else:
      print "strange..."
  else:
    shape = list_of_remaining_shapes.pop()

    for row in range(grid.max_row):
      for col in range(grid.max_col):
#        print "attempting to place", shape.id , row, col

        copy1 = copy.deepcopy(grid)
        new_list1 = list(list_of_remaining_shapes)
        if (copy1.place(shape, row, col)):
          #if not grid_is_impossible(copy1):
          recursive_solve(copy1, new_list1)

        if not shape.do_not_rotate:
          copy2 = copy.deepcopy(grid)
          new_list2 = list(list_of_remaining_shapes)
          shape.rotate_clockwise(True)
          if (copy2.place(shape, row, col)):
            #if not grid_is_impossible(copy1):
            recursive_solve(copy2, new_list2)

          if not shape.rotate_only_once:
            copy3 = copy.deepcopy(grid)
            new_list3 = list(list_of_remaining_shapes)
            shape.rotate_clockwise(True)
            if (copy3.place(shape, row, col)): 
              #if not grid_is_impossible(copy1):
              recursive_solve(copy3, new_list3)

            copy4 = copy.deepcopy(grid)
            new_list4 = list(list_of_remaining_shapes)
            shape.rotate_clockwise(True)
            if (copy4.place(shape, row, col)): 
              #if not grid_is_impossible(copy1):
              recursive_solve(copy4, new_list4)

    #list_of_remaining_shapes.append(shape)

# Test filling this case:
#
# +-----+
# |a..a.|
# |.aa..|
# |.....|
# |.....|
# |.....|
# +-----+
def test_flood_fill_algorithm1():
  print "test_flood_fill_algorith1"
  grid = Grid(5,5)
  grid.Matrix[0][0] = 1 
  grid.Matrix[1][1] = 1 
  grid.Matrix[1][2] = 1 
  grid.Matrix[0][3] = 1 
  if (grid.flood_fill((0,1),0,-1) != 2):
    print "FAIL!"


# Test filling this case:
#
# +-----+
# |.a...|
# |a.a..|
# |a..a.|
# |.aa..|
# |.....|
# +-----+
def test_flood_fill_algorithm2():
  print "test_flood_fill_algorith2"
  grid = Grid(5,5)
  grid.Matrix[0][1] = 1 
  grid.Matrix[1][0] = 1 
  grid.Matrix[1][2] = 1 
  grid.Matrix[2][0] = 1 
  grid.Matrix[2][3] = 1 
  grid.Matrix[3][1] = 1 
  grid.Matrix[3][2] = 1 
  if (grid.flood_fill((1,1),0,-1) != 3):
    print "FAIL!"

# Test filling this case:
#
# +-----+
# |a....|
# |.a...|
# |.a...|
# |.a...|
# |a....|
# +-----+
def test_flood_fill_algorithm3():
  print "test_flood_fill_algorith3"
  grid = Grid(5,5)
  grid.Matrix[0][0] = 1 
  grid.Matrix[1][1] = 1 
  grid.Matrix[2][1] = 1 
  grid.Matrix[3][1] = 1 
  grid.Matrix[4][0] = 1 
  if (grid.flood_fill((1,0),0,-1) != 3):
    print "FAIL!"

# Test filling this case:
#
# +0123+
# 0aaa.|
# 1a...|
# +-----+
def test_flood_fill_algorithm5():
  print "test_flood_fill_algorith5"
  grid = Grid(2,4)
  grid.Matrix[0][0] = 1 
  grid.Matrix[0][1] = 1 
  grid.Matrix[0][2] = 1 
  grid.Matrix[1][0] = 1 
  grid.display()
  if (grid.flood_fill((1,1),0,-1) != 4):
    print "FAIL!"
  grid.display()

# Test filling this case:
#
# +01234+
# 0....a|
# 1...a.|
# 2...a.|
# 3...a.|
# 4....a|
# +-----+
def test_flood_fill_algorithm4():
  print "test_flood_fill_algorith4"
  grid = Grid(5,5)
  grid.Matrix[0][4] = 1 
  grid.Matrix[1][3] = 1 
  grid.Matrix[2][3] = 1 
  grid.Matrix[3][3] = 1 
  grid.Matrix[4][4] = 1 
#  grid.display()
  if (grid.flood_fill((1,4),0,-1) != 3):
    print "FAIL!"
#  grid.display()

# Test filling this case:
#
# +01234+
# 0.....|
# 1.....|
# 2.....|
# 3.....|
# 4..a..|
# +-----+
def test_flood_fill_algorithm6():
  print "test_flood_fill_algorith6"
  grid = Grid(5,5)
  grid.Matrix[4][2] = 1 
#  grid.display()
  if (grid.flood_fill((0,0),0,-1) != 24):
    print "FAIL!"
#  grid.display()

# Unit Tests
test_is_finished1()
test_is_finished2()
test_has_empty_space_on_left()
test_has_empty_space_on_top()
test_rotate_and_slide_top_left()
test_impossible_to_place()
test_regular_place()
#test_recursive_place1()
test_flood_fill_algorithm1()
test_flood_fill_algorithm2()
test_flood_fill_algorithm3()
test_flood_fill_algorithm4()
test_flood_fill_algorithm5()
test_flood_fill_algorithm6()
#print "-----------------"
#cProfile.run('test_recursive_place2()')
#cProfile.run('test_recursive_place3()')
#sys.exit(0) 


row_grid = raw_input('Rows in the grid? ')
col_grid = raw_input('Columns in the grid? ')

grid = Grid(int(row_grid), int(col_grid))

mylist = []
more_input = True
counter = 1
while more_input:
  print "l - Add L shape"
  print "j - Add J shape"
  print "e - Add E shape"
  print "2 - Add 2 shape"
  print "5 - Add 5 shape"
  print "b - Add Box"
  print "1 - Add Line"
  print "x - solve it"

  input = raw_input('> ')

  if input == 'l':
    newshape = Shape()  
    newshape.init_as_l_shape(counter)
    counter = counter + 1
    mylist.append(newshape)
  if input == 'j':
    newshape = Shape()  
    newshape.init_as_j_shape(counter)
    counter = counter + 1
    mylist.append(newshape)
  if input == 'e':
    newshape = Shape()  
    newshape.init_as_e_shape(counter)
    counter = counter + 1
    mylist.append(newshape)
  if input == '2':
    newshape = Shape()  
    newshape.init_as_2_shape(counter)
    counter = counter + 1
    mylist.append(newshape)
  if input == '5':
    newshape = Shape()  
    newshape.init_as_5_shape(counter)
    counter = counter + 1
    mylist.append(newshape)
  if input == 'b':
    newshape = Shape()  
    newshape.init_as_box(counter)
    counter = counter + 1
    mylist.append(newshape)
  if input == '1':
    newshape = Shape()  
    newshape.init_as_line(counter)
    counter = counter + 1
    mylist.append(newshape)
  if input == 'x':
    if len(mylist) * 4 != int(row_grid) * int(col_grid):
      print "Invalid Input!"
      sys.exit(0)
    more_input = False 

shuffle(mylist)
recursive_solve(grid, mylist)
