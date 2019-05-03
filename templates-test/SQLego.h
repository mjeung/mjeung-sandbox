#include "Lego.h"
#include <sstream>

class SQLego : public Lego<std::string,int>
{
    public:
      void doSomething();
};

void SQLego::doSomething()
{
    std::cout << "SQ receiving " << *input << " from upstream" << std::endl;

    std::stringstream inputStream(*input); 
    inputStream >> output; 

    // Stand-in processing
    std::cout << "SQ incrementing by one" << std::endl;
    output = output + 1;
  
    std::cout << "SQ setting output to " << output << std::endl;
}