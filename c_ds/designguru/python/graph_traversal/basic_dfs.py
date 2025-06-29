class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.adjacencyList = [[] for _ in range(vertices)]  # Adjacency list

    # Method to add an edge to the graph
    def addEdge(self, source, destination):
        self.adjacencyList[source].append(destination)
        self.adjacencyList[destination].append(source)  # For an undirected graph

    # Method to perform DFS using a stack
    def DFS(self, startVertex):
        visited = [False] * self.vertices  # Track visited nodes
        stack = []  # Stack for traversal

        stack.append(startVertex)  # Start with the given vertex

        while stack:
            current = stack.pop()  # Pop a vertex from the stack

            if not visited[current]:
                print(current, end=" ")  # Process the current node
                visited[current] = True  # Mark it as visited

            # Push all unvisited neighbors onto the stack
            for neighbor in self.adjacencyList[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)


class Solution:
    @staticmethod
    def main():
        g = Graph(5)

        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(0, 3)
        g.addEdge(1, 2)
        g.addEdge(2, 4)

        print("DFS Traversal starting from vertex 0: ", end="")
        g.DFS(0)


Solution.main()
