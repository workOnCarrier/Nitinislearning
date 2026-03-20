


#include <iostream>
#include <deque>

template<int N = 5>
int get_int(){
    return N;
}

template<int N, typename C >
struct GenData{
    static void gen_data(C& cont){
        cont.push_back(N);
        GenData<N -1, C>::gen_data(cont);
    }
};
template<typename C >
struct GenData<0, C>{
    static void gen_data(C& cont){
        cont.push_back(0);
    }
};
template<int N, typename C>
void gen_data(C& cont){
    GenData<N, C>::gen_data(cont);
}
void test_template_generation(){
    std::deque<int> que;
    gen_data<10>(que);
    std::cout << "Queue data: " ; for( auto & val: que) {std::cout << " " << val;} std::cout << std::endl;
}

int main (){
    test_template_generation();
    std::cout << "Hello World" << std::endl;
    std::cout << get_int<10>() << std::endl;
    std::cout << get_int() << std::endl;
    return 0;
}