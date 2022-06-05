#include "graph_t.h"
#include <iostream>
#include <string>

void test_graph_t();

int main(){
    test_graph_t();
    return 0;
}
void test_graph_t(){
    std::string london = "London";
    std::string delhi = "Delhi";
    std::string mumbai = "Mumbai";
    std::string pune = "Pune";
    std::string unknown = "Unknown";
    auto cities = std::vector<std::string>({london, delhi, mumbai, pune});
    
    auto graph_obj = GraphT<std::string>(cities, true);
    graph_obj.add_edge(london, delhi);
    graph_obj.add_edge(delhi, mumbai);
    graph_obj.add_edge(delhi, pune);
    graph_obj.add_edge(delhi, unknown);
    graph_obj.printGraph(std::cout);
    // for (auto city : cities){
    //     std::cout << "city" << city << std::endl;
    // }
}