#include "Buffer_Struct.h"
#include <map>

class RASM
{

public:
  void start(int key, int expected_size);
  void append(int key, char * buffer, int buffer_size);
  bool is_done(int key);
  char * get_buffer(int key);
  void remove(int key);

  int active_nodes() { return m_asms.size(); }

private:
  typedef std::map< int, Buffer_Struct > ASM_Map;
  ASM_Map m_asms;

};
