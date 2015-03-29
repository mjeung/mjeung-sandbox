#include <iostream>
#include "RASM.h"

int main()
{
  RASM rasm; 

  int key = 900;
  char buffer[1500]; 
  char buffer_size = 10;

  for(int ii = 0; ii < 10; ++ii)
  {
    buffer[ii] = 'a' + ii;
  }

  rasm.start(key, 30);
  rasm.append(key, buffer, buffer_size);

  if (rasm.is_done(key))
    std::cout << "fail!" << std::endl;

  rasm.append(key, buffer, buffer_size);
  rasm.append(key, buffer, buffer_size);

  if (rasm.is_done(key))
    std::cout << "pass!" << std::endl;
  else
    std::cout << "fail" << std::endl;

  rasm.append(key, buffer, buffer_size);

  char * ptr = rasm.get_buffer(key);

  //for (int ii = 0; ii < 30; ++ii)
  //{
  //  std::cout << ii << ":" <<  ptr[ii] << std::endl;
  //}

 std::cout << "active nodes: " << rasm.active_nodes() << std::endl; 

  rasm.remove(key);
  rasm.append(key, buffer, buffer_size);
  rasm.is_done(key);

 std::cout << "active nodes: " << rasm.active_nodes() << std::endl; 

  return 1;
}
