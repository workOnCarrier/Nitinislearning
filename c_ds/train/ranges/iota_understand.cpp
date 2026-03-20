#include <algorithm>
#include <iostream>
#include <ranges>
using namespace std;
 
struct Bound
{
    int bound;
    bool operator==(int x) const { cout << x << " == " << bound << endl;
        return x == bound; }
};
 
int main()
{
    for (int i : std::ranges::iota_view{1, 10})
        std::cout << i << ' ';
    std::cout << '\n';
 
    for (int i : std::views::iota(0, 10))
        std::cout << i << ' ';
    std::cout << '\n';
 
    for (int i : std::views::iota(1, Bound{10})){
        std::cout << i << ' '; std::cout << '\n';
    }
 
    for (int i : std::views::iota(1) | std::views::take(9))
        std::cout << i << ' ';
    std::cout << '\n';
 
    std::ranges::for_each(std::views::iota(1, 10),
                          [](int i){ std::cout << i << ' '; });
    std::cout << '\n';
}