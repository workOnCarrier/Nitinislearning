#include <memory>
#include <iostream>
#include <list>
#include <unordered_map>
#include <vector>
#include <ostream>

template <typename Data>
class Node{
public:
    Data  m_data;
    std::list<Data>  m_neighbours;
    Node(Data data):m_data(data){}
    static std::shared_ptr<Node> create(Data data){return std::make_shared<Node>(data);}
};


template<typename Data,
        typename NodeData = Node<Data>,
        typename NodeDataPtr = std::shared_ptr<NodeData>>
class GraphT{
    // all Nodes
    // hashmap (string, NodePtr)
    typedef std::unordered_map<std::string, NodeDataPtr> NodeList;
    std::unordered_map<std::string, NodeDataPtr> m_node_list;
    int       m_node_count;
    bool      m_directed;
public:
    GraphT(const std::vector<Data>& dataset, bool directed=false)
    : m_node_count(dataset.size()), m_directed(directed) {
        for (auto item: dataset){
            auto value = NodeData::create(item);
            m_node_list[item] =  value;
        }
    }
    void protected_add_edge(Data source, Data dest){
        try{
            m_node_list[source]->m_neighbours.push_back(dest);
        }catch(...){
            std::cout << "Exception in add_edge" << std::endl;
            throw;
        }
    }
    void add_edge(Data source, Data dest){
        protected_add_edge(source, dest);
        if (!m_directed){
            protected_add_edge(dest, source);
        }
    }
    // const NodeList getNodeList() const{return m_node_list;}
    void printGraph(std::ostream& stream){
        for (auto pair : m_node_list){
            stream << pair.first << "-->";
            for (auto nbr : pair.second->m_neighbours){
                stream << "\t" << nbr  ;
            }
            stream << std::endl;
        }
    }
    void printGraph_Archimate(std::ostream& stream, std::string name){
        std::string start_string = "@startuml ";
        stream << start_string;
        stream << name << "\n!include <archimate/Archimate>\n";
        int running_num = 0;
        for(auto pair: m_node_list){
            for (auto nbr: pair.second->m_neighbours){
                stream << "Rel_Access_w(" << pair.first << ", " << nbr <<
                 "," << running_num++ << ")\n";
            }
        }
        std::string end_string = "@enduml";
        stream << end_string;
    }

};