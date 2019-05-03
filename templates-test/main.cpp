#include <iostream>

#include "Lego.h"

class ConcreteLego : public Lego<int,std::string>
{
    public:
      void doSomething();
};

void ConcreteLego::doSomething()
{
  // Developer writes this

  std::cout << "CONCRETE LEGO DO SOMETHING" << std::endl;
  input = 50;
  output = "string output";

  std::cout << "int input :"  << input << std::endl;
  std::cout << "string output:"  << output << std::endl;
}

int main()
{
    Lego<int,int> l1;
    std::cout << "Lego<int,int>" << std::endl;
    l1.describeOutput();
    l1.subscribe();
    l1.doSomething();

    std::cout << "-----" << std::endl;

    Lego<int,std::string> l2;
    std::cout << "Lego<int,string>" << std::endl;
    l2.describeOutput();
    l2.subscribe();
    l2.doSomething();

    std::cout << "-----" << std::endl;

    Lego<std::string,int> l3;
    std::cout << "Lego<string,int>" << std::endl;
    l3.describeOutput();
    l3.subscribe();
    l3.doSomething();

    std::cout << "-----" << std::endl;

    Lego<std::string,std::string> l4;
    std::cout << "Lego<string,string>" << std::endl;
    l4.describeOutput();
    l4.subscribe();
    l4.doSomething();

    std::cout << "-----" << std::endl;

    ConcreteLego concrete;
    concrete.describeOutput();
    concrete.subscribe();
    concrete.doSomething();

    return 1;
}