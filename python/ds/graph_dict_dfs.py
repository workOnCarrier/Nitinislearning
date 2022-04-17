from python.ds.graph_dict import GraphDict
from python.ds.graph_to_puml import graph_dict_to_puml


def graph_dict_dfs(graph: GraphDict, vertex, operator: callable):
    visited = set()
    visited.add(vertex)
    stack = [vertex, ]
    while stack:
        current_vertex = stack.pop()
        operator(current_vertex)
        for adj in graph.edges(current_vertex):
            if adj not in visited:
                stack.append(adj)
                visited.add(adj)


def graph_dict_dfs_recur(graph: GraphDict, vertex, operator: callable, visited: list = list()):
    visited = visited
    operator(vertex)
    visited.append(vertex)
    for adj_vertex in graph.edges(vertex):
        if adj_vertex not in visited:
            graph_dict_dfs_recur(graph, adj_vertex, operator, visited)


def graph_dict_post_process_recur(graph: GraphDict, vertex, operator: callable, visited: list = list()):
    visited = visited
    visited.append(vertex)
    for adj_vertex in graph.edges(vertex):
        if adj_vertex not in visited:
            graph_dict_post_process_recur(graph, adj_vertex, operator, visited)
    operator(vertex)


def graph_dict_post_process(graph: GraphDict, vertex, operator: callable):
    visited = [vertex]
    stack = [vertex]
    while stack:
        vertex = stack.pop()
        visited.append(vertex)
        for adj_vertex in graph.edges(vertex):
            if adj_vertex not in visited:
                stack.append(adj_vertex)
        operator(vertex)


def trial_graph_dict_bfs():
    custom_dict = {
        'a': ['b', 'c'],
        'b': ['a', 'd', 'e'],
        'c': ['a', 'e'],
        'd': ['b', 'e', 'f'],
        'e': ['d', 'f', 'c'],
        'f': ['d', 'e']
    }
    graph = GraphDict(custom_dict)
    operation_1 = lambda x: print(x)
    puml_file = 'graph_dict.puml'
    graph_dict_to_puml(graph, puml_file)
    graph_dict_dfs(graph, 'a', operation_1)
    print('*' * 20)
    graph_dict_dfs_recur(graph, 'a', operation_1)
    print('*' * 20)
    graph_dict_post_process_recur(graph, 'a', operation_1)


if __name__ == '__main__':
    trial_graph_dict_bfs()
