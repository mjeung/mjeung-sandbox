#!C:\Python25\python.exe

class Page(object):
	def __init__(self, start=-1, end=-1):
		self.start=start
		self.end=end
		
	start=None
	end=None

def allocate_new_page(s,x,used_list):
	newPage = Page()
	newPage.start = s
	newPage.end = s + x - 1
	used_list.append(newPage);
	return newPage.start
	
def allocate(free_list,used_list,x):
	for page in free_list:
		free_chunk_size = page.end - page.start + 1
		if (free_chunk_size > x):
			addr = allocate_new_page(page.start, x, used_list);
			page.start = page.start + x  # resize the chunk
			return addr;
		elif free_chunk_size == x:
			addr = allocate_new_page(page.start, x, used_list);
			free_list.remove(page)  # remove the chunk
			return addr;

	return -1;
	
def printPage(p):
	print "Page:", p.start, "-", p.end
	
def free(free_list,used_list,addr):
	success = False
	for pageToDelete in used_list:
		if pageToDelete.start == addr:
			success = True
			
			ptd = pageToDelete
			used_list.remove(pageToDelete)
			
			mergeDown = False
			for page in free_list:
				if (page.end + 1 == ptd.start):
					# print "mergeDownCase:"
					# printPage(page)
					# print "to"
					# printPage(ptd)
					page.end = ptd.end
					mergeDown = True
					ptd = page
					break;
			
			mergeUp = False
			for page in free_list:
				if (page.start - 1 == ptd.end):
					# print "mergeUpCase"
					# printPage(page)
					# print "to"
					# printPage(ptd)
					page.start = ptd.start
					mergeUp = True
					
					if (mergeUp and mergeDown):
						free_list.remove(ptd)
					
					break;
			

			
			if (mergeUp == False and mergeDown==False):
				newPage = Page(ptd.start,ptd.end)
				free_list.append(newPage)
						
			break;

	if success == False:
		print "couldn't find address", addr
	if success == True:
		print "done"
	
free_list = []
used_list = []

def getKey(page):
	return page.start

while(1):
	user_input = raw_input('> ')
	words = user_input.split()
	
	command = words[0]
	
	if command == "init":
	  size = words[1]
	  p = Page(0,int(size) - 1)
	  free_list = [p]
	  used_list = []
	  print "done"
	  
	elif command == "allocate":
	  size = int(words[1])
	  address = allocate(free_list,used_list,size)
	  if address != -1:
	    print "your address is", address
	  else:
	  	print "unable to comply, not enough contiguous space"
	  
	elif command == "free":
	  addr = int(words[1])
	  free(free_list,used_list,addr)
	  
	elif command == "print":

	  u = sorted(used_list, key=getKey)
	  f = sorted(free_list, key=getKey)
	  print "FREE SPACE"
	  for page in f:
		print page.start,"-",page.end,"(size:",page.end-page.start+1,")"
	  print "USED SPACE"
	  for page in u:
		print page.start,"-",page.end,"(size:",page.end-page.start+1,")"
	  
	else:
	  print "invalid command"
	