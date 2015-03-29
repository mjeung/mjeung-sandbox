#ifndef ASM_NODE_H
#define ASM_NODE_H

struct ASM_Node
{
  ASM_Node();
  ASM_Node(int k, int es);

  int key;
  char buffer[1600];
  int current_size;
  int expected_size;
};

#endif
