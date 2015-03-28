#include "Buffer_Struct.h"
#include <stdio.h>
#include <string.h>

Buffer_Struct::Buffer_Struct() :
  key(0),
  current_size(0),
  expected_size(0)
{
  memset(buffer,0,1600);
}

Buffer_Struct::Buffer_Struct(int k, int es) :
  key(k),
  current_size(0),
  expected_size(es)
{
  memset(buffer,0,1600);
}

