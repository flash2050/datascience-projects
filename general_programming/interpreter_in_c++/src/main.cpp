#include <string>
#include <iostream>
#include "repl.h"


int main() {
    std::cout << "Hello! This is the Monkey programming language \n";
    std::cout << "Feel free to type in commands. \n";

    // std::istream input_stream = std::stdin;
    repl::Start(std::cin, std::cout);
}
