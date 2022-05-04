#include <iostream>
#include <stdlib.h>
#include <vector>
#include <utility>
#include "graph_adt.h"
#include "graph_io.h"
#include "graph_cc.h"


using namespace std;

int test_display_graph( int vertices){
    Graph graph(vertices, true);
    IO<Graph>::scan(graph);
    if (vertices < 20)IO<Graph>::show(graph);
    cout << graph.EdgesCount() << "edges";
    ConnectivityCheck<Graph> graph_cc(graph);
    cout << graph_cc.count() << "components" << endl;
    return 0;
}

void test_add_adj_list_to_graph(){
    int vertices_count = 5;
    vector<pair<int, int>> edge_list = {{0,1}, {0,2}, {0,3},
    {0,4}, {0,5}};
    Graph graph(vertices_count, false);
    for (size_t edge_count = 0; edge_count < edge_list.size();
    edge_count ++){
        Edge edge = Edge(edge_list[edge_count].first, edge_list[edge_count].second);
        graph.insert(edge);
    }
}

int main(int argc, char* argv[]){
    int vertices = atoi(argv[1]);
    test_display_graph(vertices);
    return 0;
}