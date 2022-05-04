#include <vector>
using std::vector;

struct Edge{
    int v, w;
    Edge(int v = -1, int w = -1){}
};

class Graph{
private:
public:
    Graph(int, bool);
    Graph() {};
    virtual ~Graph() = 0;
    virtual int VerticesCount()const;
    virtual int EdgesCount()const;
    virtual bool directed() const;
    virtual void insert(Edge);
    virtual void remove(Edge);
    virtual bool edge(int, int) const;

    class AdjIterator{
    public:
        AdjIterator(const Graph &, int);
        int beg();
        int next();
        bool end();

    };

};

template<typename Graph>
vector<Edge> edges(Graph &graph){
    int E = 0;
    vector<Edge> a(graph.EdgesCount());
    for (int curr=0; curr < graph.VerticesCount(); v++){
        typename graph.AdjIterator adj_iterator(graph, curr);
        for ( int adj_item = adj_iterator.beg();
                !adj_iterator.end();
                adj_item=adj_iterator.next()){
                    if (graph.directed() || curr < adj_item){
                        a[E++] = Edge(curr, adj_item);
                    }
        })
    }
    return a;
}

class GraphDense: public Graph{
    int m_vert_count, m_edge_count; bool m_digraph; vector<vector<bool>> adj_matrix;
public:
    ~GraphDense(){}
    GraphDense() = delete;
    GraphDense(int vertex_count, bool digraph = false):
        m_vert_count(vertex_count),
        m_edge_count(0),
        m_digraph(digraph),
        adj_matrix(vertex_count){
            for (int i = 0; i < vertex_count; i++){
                adj_matrix[i].assign(vertex_count, false);
            }
    }
    int VerticesCount()const override {return m_vert_count;}
    int EdgesCount()const override {return m_edge_count;}
    bool directed() const override {return m_digraph;}
    virtual void insert(Edge e) override {
        int v = e.v, w = e.w;
        if (adj_matrix[v][w] == false) m_edge_count++;
        adj_matrix[v][w] = true;
        if (!m_digraph) adj_matrix[w][v] = true;
    }
    virtual void remove(Edge e) override{
        int v = e.v, w = e.w;
        if (adj_matrix[v][w] == true) m_edge_count--;
        adj_matrix[v][w] =false;
        if (!m_digraph) adj_matrix[w][v] = false;
    }
    virtual bool edge(int v, int w) const override{
        return adj_matrix[v][w];
    }
    class AdjIterator;
    friend class AdjIterator;

};

class GraphDense::AdjIterator{
    const GraphDense &m_graph;
    int curr_index, curr_vector;
public:
    AdjIterator(const GraphDense& graph, int vertex):
    m_graph(graph), curr_vector(vertex), curr_index(-1){}
    int next(){
        for(curr_index++; curr_index < m_graph.VerticesCount(); curr_index++){
            if (m_graph.adj_matrix[curr_vector][curr_index] == true) return curr_index;
        }
        return -1;
    }
    int beg(){curr_index=-1; return next();}
    bool end(){
        return curr_index >= m_graph.VerticesCount();
    }
};

class GraphSparse: public Graph{
    int m_vertex_count, m_edge_count;
    bool m_is_digraph;
    struct Node{
        int m_dest_vertex;
        struct Node* m_next;
        Node(int vertex, Node* next):m_dest_vertex(vertex), m_next(next){}
    };
    typedef Node* Link;
    vector<Link> m_adj_list;
public:
    GraphSparse(int vertex_count, bool digraph): m_vertex_count(vertex_count),
        m_edge_count(0), m_is_digraph(digraph), m_adj_list(vertex_count){
            m_adj_list.assign(vertex_count,0);
        }
    int VerticesCount() const override {return m_vertex_count;}
    int EdgesCount() const override {return m_edge_count;}
    bool directed() const override {return m_is_digraph;}
    void insert(Edge e) override{ 
        int v = e.v, w = e.w;
        // add a check to confirm if the edge already exists
        m_adj_list[v] = new Node(w, m_adj_list[v]);
        if (!m_is_digraph) m_adj_list[w] = new Node(v, m_adj_list[w]);
        m_edge_count++;
    }
    void remove(Edge e) override{
        // remove the edge from the linked lists for v and w
    }
    bool edge(int v, int w) const  override {
        // search the edge for v with w and vice-versa
        return false;
    }
    class AdjIterator;
    friend class AdjIterator;

};


class GraphSparse::AdjIterator{
    GraphSparse& m_graph;
    int m_vertex;
    Link m_temp;
public:
    AdjIterator(GraphSparse& graph, int vertex):m_graph(graph), m_vertex(vertex), m_temp(NULL) {}
    int beg(){
        m_temp = m_graph.m_adj_list[m_vertex];
        return m_temp != NULL ? m_temp->m_dest_vertex: -1;
    }
    int next(){
        if (m_temp) m_temp = m_temp->m_next; 
        return m_temp != NULL ? m_temp->m_dest_vertex: -1;
    }
    bool end(){
        return m_temp == NULL;
    }
};
