


#include <iostream>

template<int N = 5>
int get_int(){
    return N;   
}

int main (){
    std::cout << "Hello World" << std::endl;
    std::cout << get_int<10>() << std::endl;
    std::cout << get_int() << std::endl;
    return 0;
}