#include <iostream>


template< unsigned long long N >
struct binary
{
  enum { value = (N % 8) + 2 * binary< N / 8 > :: value } ;
};

template<>
struct binary< 0 >
{
  enum { value = 0 } ;
};

int BOOST_BINARY(int a){
    int b = 0;
    
    for (int i = 0;i < 8;i++){
        b += a % 10 << i;
        a = a / 10;
    }
    
    return b;
}


int main(){
    std::cout << BOOST_BINARY(101010) << std::endl;
    return 0;
}