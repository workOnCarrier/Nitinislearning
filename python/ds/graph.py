#  Adjacency matrix
#  Adjacency list

class Graph:
    def __init__(self, directed: bool = False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for key, value in self.adj_list.items():
            print(f'{key} : {value}')

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            if self.directed is False:
                self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                if self.directed is False:
                    self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, v):
        if v in self.adj_list.keys():
            if self.directed is False:
                for other_vertex in self.adj_list[v]:
                    self.adj_list[other_vertex].remove(v)
            del self.adj_list[v]
            return True
        return False

    def vertices(self):
        return self.adj_list.keys()

    def edges(self, vertex):
        return self.adj_list[vertex]


def graph_dfs_process(graph: Graph, vertex, processor: callable):
    to_process = []
    to_visit = [vertex]
    while to_visit:
        curr_vertex = to_visit.pop()
        if not processor.processed(curr_vertex) and curr_vertex not in to_process:
            to_process.insert(0, curr_vertex)
        for vertex in graph.adj_list[curr_vertex]:
            if vertex not in to_process and not processor.processed(vertex):
                to_visit.append(vertex)
    for item in to_process:
        processor(item)


class MyStack():
    def __init__(self):
        self.__stack = []

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        return self.__stack.pop()

    def __len__(self):
        return len(self.__stack)


def graph_dfs_walk(graph: Graph):
    to_visit = MyStack()
    final = []

    def processed(processed_list, edges) -> bool:
        is_processed = True
        for edge in edges:
            if edge not in processed_list:
                is_processed = False
        return is_processed

    def walk_vertex():
        while to_visit:
            cv = to_visit.pop()
            if cv in final:
                continue
            edges = graph.edges(cv)
            if not edges or processed(final, edges):
                final.insert(0, cv)
            else:
                to_visit.push(cv)
                for v_next in graph.edges(cv):
                    if v_next not in final:
                        to_visit.push(v_next)

    for vertex in graph.vertices():
        to_visit.push(vertex)
        walk_vertex()
    return final


def my_topological_sort(graph):
    class Processor:
        def __init__(self, result_: list):
            self.result = result_

        def processed(self, value) -> bool:
            return value in self.result

        def __call__(self, value):
            self.result.insert(0, value)

    result = []

    stack_push = Processor(result)
    for v in graph.vertices():
        graph_dfs_process(graph, v, stack_push)

    return result
