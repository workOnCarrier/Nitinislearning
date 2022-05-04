from python.ds.graph import Graph, my_topological_sort, graph_dfs_walk
from python.ds.graph_to_puml import graph_adjlist_to_puml
from python.ds.topological_sort import topological_sort


def test_empty_graph():
    print('\tempty graph')
    sample_graph = Graph()
    sample_graph.add_vertex('A')
    sample_graph.print_graph()


def try_graph_with_vertex():
    print('\tadd vertex with edge')
    sample_graph = Graph()
    sample_graph.add_vertex('A')
    sample_graph.add_vertex('B')
    sample_graph.add_edge('A', 'B')
    sample_graph.print_graph()


def try_graph_add_remove_edge():
    print('\t graph edge removal start state')
    sample_graph = Graph()
    sample_graph.add_vertex('A')
    sample_graph.add_vertex('B')
    sample_graph.add_vertex('C')
    sample_graph.add_vertex('D')
    sample_graph.add_edge('A', 'B')
    sample_graph.add_edge('A', 'C')
    sample_graph.add_edge('B', 'C')
    sample_graph.print_graph()

    sample_graph.remove_edge('A', 'C')
    sample_graph.remove_edge('A', 'D')
    print('\t graph edge removal end state')
    sample_graph.print_graph()


def try_graph_add_remove_vertex():
    print('\t graph edge removal start state')
    sample_graph = Graph()
    sample_graph.add_vertex('A')
    sample_graph.add_vertex('B')
    sample_graph.add_vertex('C')
    sample_graph.add_vertex('D')
    sample_graph.add_edge('A', 'B')
    sample_graph.add_edge('A', 'C')
    sample_graph.add_edge('A', 'D')
    sample_graph.add_edge('B', 'D')
    sample_graph.add_edge('C', 'D')
    sample_graph.print_graph()

    sample_graph.remove_vertex('D')
    print('\t graph edge removal end state')
    sample_graph.print_graph()
    puml_file = "graph_removal_try_output.puml"
    graph_adjlist_to_puml(sample_graph, puml_file)


def try_graph_dfs():
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
    graph.add_edge('c', 'f')
    graph.add_edge('e', 'h')
    graph.add_edge('e', 'f')
    graph.add_edge('f', 'g')
    graph.add_edge('b', 'c')
    graph.add_edge('b', 'd')
    graph.add_edge('d', 'f')
    puml_file = "graph_adjlist.puml"
    graph_adjlist_to_puml(graph, puml_file)

    his_result = topological_sort(graph)
    #
    # for item in my_result:
    #     print(item, end=' ')
    # print('')
    # print('-*-'*10)
    for item in his_result:
        print(item, end=' ')

    dfs_walk_result = graph_dfs_walk(graph)
    print("\nmy values")
    for vertex in dfs_walk_result:
        print(vertex, end=' ')


if __name__ == '__main__':
    # test_empty_graph()
    # try_graph_with_vertex()
    # try_graph_add_remove_edge()
    # try_graph_add_remove_vertex()
    try_graph_dfs()
