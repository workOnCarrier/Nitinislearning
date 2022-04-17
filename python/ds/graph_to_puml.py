import io

from python.ds.graph import Graph
from python.ds.graph_dict import GraphDict

start_uml = "@startuml\n!include<archimate/Archimate>"
end_uml = "\n@enduml"


def graph_adjlist_to_puml_double(graph: Graph, puml_file_name: str):
    string_stream = io.StringIO()
    index = 1;
    for key in graph.adj_list.keys():
        for link in graph.adj_list[key]:
            string_stream.write(f'\nRel_Access({key}, {link}, {index})')
            index += 1
    with open(puml_file_name, 'w+') as file_writer:
        file_writer.write(start_uml)
        file_writer.write('\n')
        file_writer.write(string_stream.getvalue())
        file_writer.write('\n')
        file_writer.write(end_uml)
    string_stream.close()


def graph_adjlist_to_puml_single(graph: Graph, puml_filename: str ):
    string_stream = io.StringIO()
    dict_rep = graph.adj_list
    processed = {}
    index = 1
    for key in dict_rep.keys():
        for link in dict_rep[key]:
            if link not in processed.keys() or \
                    (link in processed.keys() and key not in processed[link]):
                string_stream.write(f'\nRel_Access({key}, {link}, {index})')
                if key not in processed.keys():
                    processed[key] = []
                processed[key].append(link)
            index += 1
    with open(puml_filename, 'w+') as file_writer:
        file_writer.write(start_uml)
        file_writer.write(string_stream.getvalue())
        file_writer.write(end_uml)
    string_stream.close()


def graph_adjlist_to_puml(graph: Graph, puml_file_name: str, single: bool = True):
    if single is True:
        graph_adjlist_to_puml_single(graph, puml_file_name)
    else:
        graph_adjlist_to_puml_double(graph, puml_file_name)


def graph_dict_to_puml_double(graph: GraphDict, puml_file_name: str):
    string_stream = io.StringIO()
    dict_rep = graph.gdict()
    index = 1
    for key in dict_rep.keys():
        for link in dict_rep[key]:
            string_stream.write(f'\nRel_Access({key}, {link}, {index})')
            index += 1
    with open(puml_file_name, 'w+') as file_writer:
        file_writer.write(start_uml)
        file_writer.write('\n')
        file_writer.write(string_stream.getvalue())
        file_writer.write('\n')
        file_writer.write(end_uml)
    string_stream.close()


def graph_dict_to_puml_single(graph: GraphDict, puml_file_name: str):
    string_stream = io.StringIO()
    dict_rep = graph.gdict()
    processed = {}
    index = 1
    for key in dict_rep.keys():
        for link in dict_rep[key]:
            if link not in processed.keys() or \
                    (link in processed.keys() and key not in processed[link]):
                string_stream.write(f'\nRel_Access({key}, {link}, {index})')
                if key not in processed.keys():
                    processed[key] = []
                processed[key].append(link)
            index += 1
    with open(puml_file_name, 'w+') as file_writer:
        file_writer.write(start_uml)
        file_writer.write('\n')
        file_writer.write(string_stream.getvalue())
        file_writer.write('\n')
        file_writer.write(end_uml)
    string_stream.close()


def graph_dict_to_puml(graph: GraphDict, puml_file_name: str, single: bool = False):
    if not single:
        graph_dict_to_puml_double(graph, puml_file_name)
    else:
        graph_dict_to_puml_single(graph, puml_file_name)
