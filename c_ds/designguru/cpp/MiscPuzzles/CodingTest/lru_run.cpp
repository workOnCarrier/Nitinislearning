#include "lru.h"

void run_test(){
    LRU<int>  cache(3);
    std::cout << "\tputting:" << 10 << std::endl;
    cache.put(1, 10);
    std::cout << "\tputting:" << 20 << std::endl;
    cache.put(2, 20);
    std::cout << "\t getting:" << 1 << std::endl;
    std::cout << cache.get(1) << std::endl;
    std::cout << "\t getting:" << 2 << std::endl;
    std::cout << cache.get(2) << std::endl;
}

int main(){
    run_test();
}

