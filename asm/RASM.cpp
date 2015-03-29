#include "RASM.h"
#include "ASM_Node.h"
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <stdexcept>

RASM::RASM() : 
  m_invalid_expected_size(0),
  m_append_to_invalid_key(0),
  m_node_overfill(0),
  m_is_done_for_invalid_key(0),
  m_get_buffer_for_invalid_key(0),
  m_remove_for_invalid_key(0),
  m_unspecified_error(0)
{
  m_asms.clear(); 
}

void RASM::start(int key, int expected_size)
{
  if (expected_size > 1600)
  {
    std::cerr << "Invalid expected size: " << expected_size << std::endl;
    ++m_invalid_expected_size;
  }
  else
  {
    m_asms[key] = ASM_Node(key, expected_size);
  }
}

void RASM::append(int key, char * buffer, int buffer_size)
{
  ASM_Map::iterator iter = m_asms.find(key);

  if (iter != m_asms.end())
  {
    int current_size = iter->second.current_size;
    int expected_size = iter->second.expected_size;
    if ( current_size + buffer_size > expected_size)
    {
      std::cout << "OVERFILL:" << key << std::endl;
      ++m_node_overfill;
    }
    else
    {
      ASM_Node & asm_node = (iter->second);
      memcpy(&asm_node.buffer[current_size+1],buffer,buffer_size);
      m_asms[key].current_size += buffer_size;
    }
  }
  else
  {
    ++m_append_to_invalid_key;
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
  else
  {
    ++m_is_done_for_invalid_key;
  }

  return false;
}

const char * RASM::get_buffer(int key)
{
  ASM_Map::const_iterator iter = m_asms.find(key);
  if (iter != m_asms.end())
  {
    const ASM_Node & asm_node = (iter->second);
    return asm_node.buffer;
  }
  else
  {
    ++m_get_buffer_for_invalid_key;
    return NULL;
  } 
}

void RASM::remove(int key)
{
  ASM_Map::iterator iter = m_asms.find(key);
  if (iter == m_asms.end())
  {
    ++m_remove_for_invalid_key;
  }
  else
  {
    m_asms.erase(iter);
  }
}

int RASM::active_nodes() const 
{ 
  return m_asms.size(); 
}

void RASM::display_status() const
{
  std::cout << "RASM Status" << std::endl;
  std::cout << "  Invalid Expected Size: " << m_invalid_expected_size << std::endl;
  std::cout << "  Append To Invalid Key: " << m_append_to_invalid_key << std::endl;
  std::cout << "  Node Overfill: " << m_node_overfill << std::endl;
  std::cout << "  Is_Done Invalid Key: " << m_is_done_for_invalid_key << std::endl;
  std::cout << "  Get_Buffer For Invalid Key: " << m_get_buffer_for_invalid_key << std::endl;
  std::cout << "  Remove For Invalid Key: " << m_remove_for_invalid_key << std::endl;
  std::cout << "  Unspecified Error Condition: " << m_unspecified_error << std::endl;
}
