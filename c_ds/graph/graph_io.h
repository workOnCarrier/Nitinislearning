template <class Graph>
class IO{
    public:
    static void show(const Graph&);
    static void scanEZ(Graph&);
    static void scan(Graph&);
};

template<typename TGraph>
void IO<TGraph>::show(const TGraph& graph){
    for (int s=0; s < graph.Vertices(); s++){
        cout.width(2); cout << s << ":";
        typename TGraph::AdjIterator adj_iter(graph, s);
        for(int adj_item = adj_iter.beg(); !adj_iter.end(); adj_item = adj_iter.next()){
            cout.width(2); cout << adj_item << " ";
        }
        cout << endl;
    }
}

template<typename TGraph>
void IO<TGraph>::scanEZ(TGraph& graph){
    for ( int curr_edge = 0; curr_edge < graph.EdgeCount(); curr_edge ++ ){
        int index_1, index_2;
        cin >> index_1 >> index_2 ;
        edge = Edge(index_1, index_2);
        graph.insert(edge);
    }
}