#ifndef LEGO_H
#define LEGO_H

#include <iostream>
#include <string>

template <typename InputType = int, typename OutputType = int>
class Lego
{
  public:
   void subscribe(InputType * upstream);
   void describeOutput();
   void doSomething();

   InputType * input;
   OutputType output;
};

// -------------------------

template <>
void Lego<int,int>::subscribe(int * upstream)
{
  std::cout << "<int,int> Subscribing to int type"  << std::endl;
  input = upstream;
} 

template <>
void Lego<int,std::string>::subscribe(int * upstream)
{
  std::cout << "<int,string> Subscribing to int type"  << std::endl;
  input = upstream;
} 

template <>
void Lego<std::string,int>::subscribe(std::string * upstream)
{
  std::cout << "<string,int> Subscribing to string type"  << std::endl;
  input = upstream;
} 

template <>
void Lego<std::string,std::string>::subscribe(std::string * upstream)
{
  std::cout << "<string,string> Subscribing to string type"  << std::endl;
  input = upstream;
} 

// -----------------------------
// --- DEBUG FUNCTIONS BELOW ---
// -----------------------------

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

// ---------------------------------------------
// --- Vestigial Functions, no longer needed ---
// ---------------------------------------------

/* 
template <>
void Lego<int,int>::doSomething()
{
  // Child should override.
  exit(1);
} 

template <>
void Lego<int,std::string>::doSomething()
{
  // Child should override.
  exit(1);
} 

template <>
void Lego<std::string,int>::doSomething()
{
  // Child should override.
  exit(1);
}

template <>
void Lego<std::string,std::string>::doSomething()
{
  // Child should override.
  exit(1);
}
*/

#endif