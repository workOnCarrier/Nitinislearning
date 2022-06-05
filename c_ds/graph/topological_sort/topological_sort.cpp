
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include "graph_t.h"
#include <stack>
#include <queue>
#include <set>

using namespace std;

void topological_sort();
int main(){
    topological_sort();
    return 0;
}

template <typename Data>
auto recursive_topo_sort(GraphT<Data>::NodeList& nodeList,
                        queue<Data>& node,
                        stack<Data>& result)->void{
    while(!procesing_queue.empty()){
        city = processing_queue.pop();
        node = nodeList[city];
        for (auto dest: node->m_neighbours){
            processing_queue.push(dest);
            recursive_topo_sort(nodeList, processing_queue, result);
        }
        result.push(city);
    }
} 

void topological_sort(){
    typedef string City;
    City delhi = "Delhi";
    City amritsar = "Amritsar";
    City jalandhar = "Jalandhar";
    City chandigarh = "Chandigarh";
    City dasuya = "Dasuya";
    City ludhiana = "Ludhiana";
    auto cities = vector<City>({delhi, amritsar, jalandhar, chandigarh, dasuya, ludhiana});
    auto graph_obj = GraphT(cities, true);
    graph_obj.add_edge(delhi, ludhiana);
    graph_obj.add_edge(amritsar, jalandhar);
    graph_obj.add_edge(jalandhar, ludhiana);
    graph_obj.add_edge(ludhiana, dasuya);
    graph_obj.add_edge(delhi, chandigarh);
    graph_obj.add_edge(chandigarh, dasuya);
    graph_obj.add_edge(amritsar, dasuya);
    {
        std::ofstream fout;
        auto filename = "./input_graph.puml";
        cout << "opening " << filename << endl;
        fout.open(filename, ios_base::out | ios_base::trunc);
        graph_obj.printGraph_Archimate(fout, "test_graph");
    }
    auto nodeList = graph_obj.getNodeList();
    stack<City>  result;
    queue<City>  cityQueue;
    set<City> processed;
    for (auto pair: nodeList){
        auto city = pair.first;
        cityQueue.push(city);
        recursive_topo_sort(nodeList, cityQueue, result);
    }
    for (auto city: result){
        cout << city << ", ";
    }
    cout << endl;
}
