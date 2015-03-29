#include "ASM_Node.h"
#include <stdio.h>
#include <string.h>

ASM_Node::ASM_Node() :
  key(0),
  current_size(-1),
  expected_size(0)
{
  memset(buffer,0,1600);
}

ASM_Node::ASM_Node(int k, int es) :
  key(k),
  current_size(-1),
  expected_size(es)
{
  memset(buffer,0,1600);
}

