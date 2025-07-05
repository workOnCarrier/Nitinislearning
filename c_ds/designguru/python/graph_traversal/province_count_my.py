class Solution:
    def findProvinces(self, connections):
        provinces = 0
        num_of_cities = len(connections)
        visited = [False] * num_of_cities
        def dfs(city):
            for dest in range(len(connections[city])):
                if connections[city][dest] and not visited[dest]:
                    visited[dest] = True
                    dfs(dest)
        for city in range(num_of_cities):
            if not visited[city]:
                provinces += 1
                dfs(city)

        return provinces

# Main method for testing
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    example1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution.findProvinces(example1))  # Expected Output: 2

    # Example 2
    example2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(solution.findProvinces(example2))  # Expected Output: 3

    # Example 3
    example3 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
    print(solution.findProvinces(example3))  # Expected Output: 2

