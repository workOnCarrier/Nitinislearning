
#include <iostream>

class Appliction{
    public:
    Appliction(){
        std::cout << "Appliction" << std::endl;
    }
};

template <typename T>
class CustomApp1 : public T{
    public:
    CustomApp1(){
        std::cout << "CustomApp1" << std::endl;
    }
};

template <typename T>
class Level2App : public T{
    public:
    Level2App(){
        std::cout << "Level2App" << std::endl;
    }
};




void play_with_crtp_sample_1(){
    Level2App<CustomApp1<Appliction>> level2AppObj;
    std::cout << "play_with_crtp_sample_1" << std::endl;
}

void play_with_crtp_sample_1_test(){
    class ApplicationMock{public:ApplicationMock(){std::cout << "this is in mock" << std::endl;}};
    Level2App<CustomApp1<ApplicationMock>> level2AppObj;
    std::cout << "play_with_crtp_sample_1_test" << std::endl;
}

template <typename T>
class CrtpBase {
    CrtpBase(){}
    friend T;
};
class Level2Type2App : public CrtpBase<Level2Type2App> {
    public:
    Level2Type2App (){
        std::cout << "Level2App" << std::endl;
    }
};

int main(){
    play_with_crtp_sample_1();
    play_with_crtp_sample_1_test();
    return 0;
}