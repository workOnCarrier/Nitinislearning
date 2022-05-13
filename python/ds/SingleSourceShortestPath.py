


from collections import defaultdict

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)
    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:

