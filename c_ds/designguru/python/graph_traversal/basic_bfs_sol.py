from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = defaultdict(list)

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)  # For undirected graph

    def BFS(self, startVertex):
        visited = [False] * self.V  # To keep track of visited vertices
        q = deque()

        visited[startVertex] = True
        q.append(startVertex)

        while q:
            currentVertex = q.popleft()
            print(currentVertex, end=" ")

            # Explore adjacent vertices
            for neighbor in self.adjList[currentVertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

if __name__ == "__main__":
    graph = Graph(5)  # Create a graph with 6 vertices

    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    graph.addEdge(2, 4)

    print("Breadth-First Traversal starting from vertex 0:")
    graph.BFS(0)
