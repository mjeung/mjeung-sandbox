#include "Lego.h"

class QSLego : public Lego<int,std::string>
{
    public:
      void doSomething();
};

void QSLego::doSomething()
{
    std::cout << "QS receiving " << *input << " from upstream" << std::endl;

    // Stand-in processing
    std::cout << "QS incrementing by one" << std::endl;
    int temp = *input + 1;
    output = std::to_string(temp);
  
    std::cout << "QS setting output to " << output << std::endl;
}