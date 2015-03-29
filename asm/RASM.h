#ifndef RASM_H
#define RASM_H

#include "ASM_Node.h"
#include <map>

class RASM
{

public:
  RASM();
  void start(int key, int expected_size);
  void append(int key, char * buffer, int buffer_size);
  bool is_done(int key);
  const char * get_buffer(int key);
  void remove(int key);

  int active_nodes() const;
  void display_status() const;

private:
  typedef std::map< int, ASM_Node > ASM_Map;
  ASM_Map m_asms;

  unsigned int m_invalid_expected_size;
  unsigned int m_append_to_invalid_key;
  unsigned int m_node_overfill;
  unsigned int m_is_done_for_invalid_key;
  unsigned int m_get_buffer_for_invalid_key;
  unsigned int m_remove_for_invalid_key;
  unsigned int m_unspecified_error;
};

#endif
