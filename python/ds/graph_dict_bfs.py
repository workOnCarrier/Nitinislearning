from queue import Queue

from python.ds.graph_dict import GraphDict
from python.ds.graph_to_puml import graph_dict_to_puml


def graph_dict_bfs(graph: GraphDict, vertex, operate: callable):
    visited = [vertex]
    queue = Queue()
    queue.put(vertex)
    while queue:
        current_vertex = queue.get()
        operate(current_vertex)
        for edge in graph.edges(current_vertex):
            if edge not in visited:
                visited.append(edge)
                queue.put(edge)


def trial_graph_dict_bfs():
    custom_dict = {
        'a': ['b', 'c'],
        'b': ['a', 'd', 'e'],
        'c': ['a', 'e'],
        'd': ['b', 'e', 'f'],
        'e': ['b', 'c', 'd', 'f'],
        'f': ['d', 'e']
    }
    graph = GraphDict(custom_dict)
    operation = lambda x: print(x)
    puml_file = 'graph_dict.puml'
    graph_dict_to_puml(graph, puml_file)
    graph_dict_bfs(graph, 'a', operation)


if __name__ == '__main__':
    trial_graph_dict_bfs()
