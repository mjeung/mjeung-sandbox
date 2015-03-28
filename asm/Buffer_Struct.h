struct Buffer_Struct
{
  Buffer_Struct();
  Buffer_Struct(int k, int es);

  int key;
  char buffer[1600];
  int current_size;
  int expected_size;
};

