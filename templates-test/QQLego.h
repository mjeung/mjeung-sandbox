#include "Lego.h"

class QQLego : public Lego<int,int>
{
    public:
      void doSomething();
};

void QQLego::doSomething()
{
  // Developer writes this
  std::cout << "QQ receiving " << *input << " from upstream" << std::endl;

  output = *input;

  // Stand-in processing
  std::cout << "QQ incrementing by one" << std::endl;
  output = output + 1;

  std::cout << "QQ setting output to " << output << std::endl;
}