#include <iostream>

#include "Lego.h"
#include "SSLego.h"
#include "SQLego.h"
#include "QSLego.h"
#include "QQLego.h"

int main()
{
    SSLego ssLego;
    SQLego sqLego;
    QQLego qqLego;
    QSLego qsLego;

    std::cout << std::endl; 
    std::cout << "Doing wiring..." << std::endl;
    // subscribe backwards: SS <--3-- SQ <--2-- QQ <--1-- QS
    qsLego.subscribe(&(qqLego.output));  // 1
    qqLego.subscribe(&(sqLego.output));  // 2
    sqLego.subscribe(&(ssLego.output));  // 3
    std::cout << std::endl; 

    ssLego.doSomething();
    std::cout << "---" << std::endl;
    sqLego.doSomething();
    std::cout << "---" << std::endl;
    qqLego.doSomething();
    std::cout << "---" << std::endl;
    qsLego.doSomething();

    return 1;
}