from collections import defaultdict, deque

class Solution:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, v, w):
        self.adj_list[v].append(w)

    def topological_sort(self):
        in_degree = [0] * self.vertices
        
        # Calculate in-degrees of all vertices
        for i in range(self.vertices):
            for neighbor in self.adj_list[i]:
                in_degree[neighbor] += 1
        
        # Create a queue and enqueue all vertices with in-degree 0
        queue = deque()
        for i in range(self.vertices):
            if in_degree[i] == 0:
                queue.append(i)
        
        count = 0  # Initialize count of visited vertices
        top_order = []  # List to store the topological order
        
        # Process vertices in the queue
        while queue:
            u = queue.popleft()  # Dequeue a vertex
            top_order.append(u)  # Add it to the topological order
            
            # Iterate through all its neighboring nodes
            for neighbor in self.adj_list[u]:
                # Reduce in-degree by 1
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)  # If in-degree becomes 0, add it to the queue
            
            count += 1  # Increment count of visited vertices
        
        # Check if there was a cycle
        if count != self.vertices:
            print("There exists a cycle in the graph")
            return
        
        # Print topological order
        print("Topological sort of the given graph:")
        print(top_order)

# Example usage
g = Solution(6)  # Create a graph with 6 vertices
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.topological_sort()  # Perform topological sort
