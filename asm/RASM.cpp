#include "RASM.h"
#include "ASM_Node.h"
#include <stdio.h>
#include <string.h>
#include <iostream>

void RASM::start(int key, int expected_size)
{
  m_asms[key] = ASM_Node(key, expected_size);
}

void RASM::append(int key, char * buffer, int buffer_size)
{
  ASM_Map::iterator iter = m_asms.find(key);

  if (iter != m_asms.end())
  {
    int current_size = iter->second.current_size;
    ASM_Node & asm_node = (iter->second);
    memcpy(&asm_node.buffer[current_size+1],buffer,buffer_size);
    m_asms[key].current_size += buffer_size;

    if ( m_asms[key].current_size > m_asms[key].expected_size)
    {
     std::cout << "OVERFILL:" << key << std::endl;
    }
  }
}

bool RASM::is_done(int key)
{
  ASM_Map::iterator iter = m_asms.find(key);

  if (iter != m_asms.end())
  {
    if (m_asms[key].current_size >= (m_asms[key].expected_size -1))
      return true;
    else
      return false;
  }

  return false;
}

char * RASM::get_buffer(int key)
{
  ASM_Map::iterator iter = m_asms.find(key);

  if (iter != m_asms.end())
  {
    ASM_Node & asm_node = (iter->second);
    return asm_node.buffer;
  }
  else
  {
    return NULL;
  } 
}

void RASM::remove(int key)
{
  m_asms.erase(key);
}
