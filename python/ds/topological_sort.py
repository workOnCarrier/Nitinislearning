from python.ds.graph import Graph
from python.ds.graph_dict_dfs import graph_dict_post_process_recur, graph_dict_post_process
from python.ds.graph_to_puml import graph_dict_to_puml, graph_adjlist_to_puml


def topological_sort_util(graph: Graph, v, visited, stack):
    visited.append(v)
    for i in graph.edges(v):
        if i not in visited:
            topological_sort_util(graph, i, visited, stack)
    stack.insert(0, v)


def topological_sort(graph: Graph):
    visited = []
    stack = []
    for k in graph.vertices():
        if k not in visited:
            topological_sort_util(graph, k, visited, stack)
    return stack


def try_run_topological_sort():
    graph = Graph(directed=True)
    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')
    graph.add_vertex('e')
    graph.add_vertex('f')
    graph.add_vertex('g')
    graph.add_vertex('h')
    graph.add_edge('a', 'c')
    graph.add_edge('c', 'e')
    graph.add_edge('e', 'h')
    graph.add_edge('e', 'f')
    graph.add_edge('f', 'g')
    graph.add_edge('b', 'c')
    graph.add_edge('b', 'd')
    graph.add_edge('d', 'f')
    file_name = 'for_topological.puml'
    graph_adjlist_to_puml(graph, file_name, single=True)
    result = topological_sort(graph)
    for item in result:
        print(item, end=" ")

if __name__ == '__main__':
    try_run_topological_sort()
    # b d a c e f g h
