from python.ds.graph_dict import GraphDict
from python.ds.graph_to_puml import graph_dict_to_puml


def try_graph_dict ():
    custom_dict = {
        "a": ['b', 'c'],
        'b': ['a', 'e', 'd'],
        'c': ['a', 'e'],
        'd': ['b', 'e', 'f'],
        'e': ['d', 'f', 'b', 'c'],
        'f': ['d', 'e']
    }
    graph = GraphDict(custom_dict)
    puml_file = 'graph_dict.puml'
    graph_dict_to_puml(graph, puml_file)

if __name__ == '__main__':
    try_graph_dict()
