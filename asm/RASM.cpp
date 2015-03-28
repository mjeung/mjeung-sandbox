#include "RASM.h"
#include <stdio.h>
#include <string.h>
#include <iostream>

void RASM::start(int key, int expected_size)
{
  m_asms[key] = Buffer_Struct(key, expected_size);
}

void RASM::append(int key, char * buffer, int buffer_size)
{
  ASM_Map::iterator iter = m_asms.find(key);

  if (iter != m_asms.end())
  {
    int current_size = iter->second.current_size;
    Buffer_Struct & buffer_struct = (iter->second);
    memcpy(&buffer_struct.buffer[current_size+1],buffer,buffer_size);
    m_asms[key].current_size += buffer_size;
  }

  if ( m_asms[key].current_size > m_asms[key].expected_size)
  {
   std::cout << "OVERFILL:" << key << std::endl;
  }
}

bool RASM::is_done(int key)
{
  if (m_asms[key].current_size >= m_asms[key].expected_size)
    return true;
  else
    return false;
}
