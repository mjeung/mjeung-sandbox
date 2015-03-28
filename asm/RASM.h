#include "Buffer_Struct.h"
#include <map>

class RASM
{

public:
  void start(int key, int expected_size);
  void append(int key, char * buffer, int buffer_size);
  bool is_done(int key);

private:
  typedef std::map< int, Buffer_Struct > ASM_Map;
  ASM_Map m_asms;

};
