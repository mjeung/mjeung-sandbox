#include "Lego.h"

class SSLego : public Lego<std::string,std::string>
{
    public:
      void doSomething();
};

void SSLego::doSomething()
{
   // Initial value for testing
   output = "7";

   std::cout << "SS setting output to " << output << std::endl;
}