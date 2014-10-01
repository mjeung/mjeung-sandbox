#!C:\Python27\python.exe

# I received this as an interview question once:
#
# Implement Malloc and Free
#
# Bombed the interview, but this is how I should have answered it

class MemoryInterface:
  def __init__(self,size):
    self.max_size = size 
    self.free_list = [(0,size-1)]
    self.used_list = [] 

  def reset(self):
    self.free_list = [(0,self.max_size-1)]
    self.used_list = [] 

  def malloc(self,alloc_size):
    for start_free_chunk, end_free_chunk in self.free_list:
      if end_free_chunk - start_free_chunk +1 > alloc_size:
        start_alloc_chunk = start_free_chunk
        end_alloc_chunk = start_alloc_chunk + alloc_size - 1
        self.used_list.append( (start_alloc_chunk, end_alloc_chunk ) )
        self.free_list.remove( (start_free_chunk, end_free_chunk ) )
        self.free_list.append( (start_free_chunk+alloc_size,end_free_chunk) )
        return start_free_chunk
      elif end_free_chunk - start_free_chunk + 1 == alloc_size:
        self.free_list.remove( (start_free_chunk, end_free_chunk) )
        self.used_list.append( (start_free_chunk, end_free_chunk) )
        return start_free_chunk
      elif end_free_chunk - start_free_chunk < alloc_size:
        pass
   
    return -1
  
  def free(self,free_addr):
    for start_used_chunk, end_used_chunk in self.used_list:
      new_free_chunk = True

      merge_up = False
      merge_up_lo = 0
      merge_up_hi = 0

      merge_down = False
      merge_down_lo = 0
      merge_down_hi = 0

      if start_used_chunk == free_addr:
        self.used_list.remove((start_used_chunk,end_used_chunk))
 
        for start_free_chunk, end_free_chunk in self.free_list:
          if start_used_chunk - 1 == end_free_chunk:
            merge_down = True
            merge_down_lo = start_free_chunk
            merge_down_hi = end_free_chunk
            new_free_chunk = False

          if end_used_chunk + 1 == start_free_chunk:
            merge_up = True
            merge_up_lo = start_free_chunk
            merge_up_hi = end_free_chunk
            new_free_chunk = False

        if merge_up and merge_down:
          self.free_list.remove( (merge_up_lo, merge_up_hi) )
          self.free_list.remove( (merge_down_lo, merge_down_hi) )
          self.free_list.append( (merge_down_lo, merge_up_hi) )
          pass
        elif merge_up:
          self.free_list.remove( (merge_up_lo, merge_up_hi) )
          self.free_list.append( (start_used_chunk, merge_up_hi) )
        elif merge_down:
          self.free_list.remove( (merge_down_lo, merge_down_hi) )
          self.free_list.append( (merge_down_lo, end_used_chunk) )
          

        if new_free_chunk:
          self.free_list.append((start_used_chunk,end_used_chunk))

        return True

    return False

  def print_status(self):
    print "free list:", self.free_list
    print "used list:", self.used_list

  def items_in_free_list(self):
    return len(self.free_list)

  def items_in_used_list(self):
    return len(self.used_list)

def run_unit_tests():
  mi = MemoryInterface(1000);

  if mi.malloc(1001) != -1:
    raise Exception("failed test")
  if mi.malloc(1000) != 0:
    raise Exception("failed test")
  if mi.malloc(1) != -1:
    raise Exception("failed test")

  mi.reset()

  if mi.malloc(1001) != -1:
    raise Exception("failed test")
  if mi.malloc(1000) != 0:
    raise Exception("failed test")
  if mi.malloc(1) != -1:
    raise Exception("failed test")

  mi.reset()

  if mi.malloc(500) != 0:
    raise Exception("failed test")
  if mi.malloc(500) != 500:
    raise Exception("failed test")
  if mi.malloc(500) != -1:
    raise Exception("failed test")

  mi.reset()

  if mi.malloc(250) != 0:
    raise Exception("failed test")
  if mi.malloc(250) != 250:
    raise Exception("failed test")
  if mi.malloc(250) != 500:
    raise Exception("failed test")
  if mi.malloc(250) != 750:
    raise Exception("failed test")
  if mi.malloc(250) != -1:
    raise Exception("failed test")

  if mi.free(2) != False:
    raise Exception("failed test")

  if mi.free(250) != True:
    raise Exception("failed test")

  if mi.free(500) != True:
    raise Exception("failed test")

  if mi.items_in_free_list() != 1:
    raise Exception("failed test")
  if mi.items_in_used_list() != 2:
    raise Exception("failed test")

  if mi.malloc(500) != 250:
    raise Exception("failed test")
  if mi.items_in_free_list() != 0:
    raise Exception("failed test")
  if mi.items_in_used_list() != 3:
    raise Exception("failed test")

  if mi.free(0) != True:
    raise Exception("failed test")
  if mi.free(750) != True:
    raise Exception("failed test")
  if mi.free(250) != True:
    raise Exception("failed test")

  if mi.items_in_free_list() != 1:
    raise Exception("failed test")
  if mi.items_in_used_list() != 0:
    raise Exception("failed test")

  print ""
  print "Congratulations, all the unit tests passed!"

run_unit_tests()

#def demo():
#  mi = MemoryInterface(3)
#  if mi.malloc(1) != 0:
#    raise Exception("failed test")
#  if mi.malloc(2) != 1:
#    raise Exception("failed test")
#  mi.free(1)
#  mi.free(0)
#
#  if mi.malloc(3) != 0:
#    raise Exception("failed test")

#demo()
