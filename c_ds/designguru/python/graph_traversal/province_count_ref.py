class Solution:
    def findProvinces(self, isConnected) -> int:
        def dfs(city):
            # For each city, mark it as visited and explore its connections
            for i in range(len(isConnected)):
                if isConnected[city][i] == 1 and not visited[i]:
                    visited[i] = True
                    dfs(i)

        visited = [False] * len(isConnected)
        provinces = 0

        for city in range(len(isConnected)):
            if not visited[city]:
                dfs(city)
                provinces += 1

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

