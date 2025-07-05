class Solution:
    def numBusesToDestination(self, routes, orig, dest):
        print(f"orig:{orig} to dest:{dest}")
        single_stop_adj_list = []
        graph = {}
        path = list()
        visited = set()
        for route, stops in enumerate(routes):
            prev = -1
            for stop in stops:
                if prev == -1:
                    prev, src, next_stop = stop, stops[-1], stop
                else:
                    prev, src, next_stop = stop, prev, stop
                single_stop_adj_list.append((src, next_stop, route+1))
        for stop_adj in single_stop_adj_list:
            src, next_stop, route = stop_adj
            if src not in graph:
                graph[src] = list()
            graph[src].append((next_stop, route))
        print(graph)
        def dfs(stop, route):
            path.append(route)
            visited.add(stop)
            paths = graph[stop]
            print(f" stop:{stop} :: dest:{dest}   || paths:{paths} --- path:{path}")
            if stop == dest:
                return True
            for next_stop, route in paths:
                if next_stop in visited:
                    continue
                if dfs(next_stop, route):
                    return True
            path.pop()
            return False

        dfs(orig, 0)

        unique_path = set()
        for val in path:
            if val != 0:
                unique_path.add(val)

        return [val for val in unique_path]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    routesA = [[2, 3, 4], [5, 6, 7, 8], [4, 5, 9, 10], [10, 12]]
    print(routesA)
    # print(solution.numBusesToDestination(routesA, 3, 12))  # Output: 3

    # Example 2
    routesB = [[1, 2, 3, 4, 5], [5, 6, 7, 8], [8, 9, 10, 11]]
    print(routesB)
    # print(solution.numBusesToDestination(routesB, 1, 11))  # Output: 3

    # Example 3
    routesC = [[1, 2, 5], [3, 6, 7], [7, 9, 10]]
    print(routesC)
    # print(solution.numBusesToDestination(routesC, 2, 10))  # Output: -1

    routes = [[1,2,7],[3,6,7]]
    print(routes)
    print(solution.numBusesToDestination(routes, 1, 6))  # Output: 1


