#include <iostream>
#include <string>

template <typename InputType = int, typename OutputType = int>
class Lego
{
  public:
   void subscribe();
   void describeOutput();
   void doSomething();

  protected:
   InputType input;
   OutputType output;
};

// -------------------------

template <>
void Lego<int,int>::subscribe()
{
  std::cout << "<int,int> Subscribing to int type"  << std::endl;
} 

template <>
void Lego<int,std::string>::subscribe()
{
  std::cout << "<int,string> Subscribing to int type"  << std::endl;
} 

template <>
void Lego<std::string,int>::subscribe()
{
  std::cout << "<string,int> Subscribing to string type"  << std::endl;
} 

template <>
void Lego<std::string,std::string>::subscribe()
{
  std::cout << "<string,string> Subscribing to string type"  << std::endl;
} 

// -------------------------

template <>
void Lego<int,int>::describeOutput()
{
  std::cout << "<int,int> My output type is int"  << std::endl;
} 

template <>
void Lego<int,std::string>::describeOutput()
{
  std::cout << "<int,string> My output type is string"  << std::endl;
} 

template <>
void Lego<std::string,int>::describeOutput()
{
  std::cout << "<string,int> My output type is int"  << std::endl;
} 

template <>
void Lego<std::string,std::string>::describeOutput()
{
  std::cout << "<string,string> My output type is string"  << std::endl;
} 

// -------------------------

template <>
void Lego<int,int>::doSomething()
{
  // Test only, normally the child overrides this
  input = 1;
  input = input * 50;
  output = input + 5000;

  std::cout << "PARENT DO SOMETHING"  << std::endl;
  std::cout << "input:"  << input << std::endl;
  std::cout << "output:"  << output << std::endl;
} 

template <>
void Lego<int,std::string>::doSomething()
{
  // Test only, normally the child overrides this
  input = 1;
  input = input * 50;
  output = "string output, input was " + std::to_string(input);

  std::cout << "PARENT DO SOMETHING"  << std::endl;
  std::cout << "input:"  << input << std::endl;
  std::cout << "output:"  << output << std::endl;
} 

template <>
void Lego<std::string,int>::doSomething()
{
  // Test only, normally the child overrides this
  input = "string input";
  output = 50;

  std::cout << "PARENT DO SOMETHING"  << std::endl;
  std::cout << "input:"  << input << std::endl;
  std::cout << "output:"  << output << std::endl;
}

template <>
void Lego<std::string,std::string>::doSomething()
{
  // Test only, normally the child overrides this
  input = "string input";
  output = "string output";

  std::cout << "PARENT DO SOMETHING"  << std::endl;
  std::cout << "input:"  << input << std::endl;
  std::cout << "output:"  << output << std::endl;
}
