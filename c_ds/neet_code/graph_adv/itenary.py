from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for a, b in tickets:
            adj[a].append(b)
        result = ['JFK']
        print(f"\t adj start : {adj}")
        def dfs(src):
            print(f"\t adj processing : {adj}")
            if len(result) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            tmplist = list(adj[src])
            for i, v in enumerate(tmplist):
                adj[src].pop(i)
                result.append(v)
                print(f"\t adj before     : {adj}")
                if dfs(v): return True
                adj[src].insert(i, v)
                result.pop()
            return False
        dfs("JFK")
        return result



def test():
    input = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    sol = Solution()
    itenary = sol.findItinerary(input)
    print(itenary)

def test2():
    input = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","ATL"],["ATL","BBB"],["BBB","ATL"],["ATL","CCC"],["CCC","ATL"],["ATL","DDD"],["DDD","ATL"],["ATL","EEE"],["EEE","ATL"],["ATL","FFF"],["FFF","ATL"],["ATL","GGG"],["GGG","ATL"],["ATL","HHH"],["HHH","ATL"],["ATL","III"],["III","ATL"],["ATL","JJJ"],["JJJ","ATL"],["ATL","KKK"],["KKK","ATL"],["ATL","LLL"],["LLL","ATL"],["ATL","MMM"],["MMM","ATL"],["ATL","NNN"],["NNN","ATL"]]
    sol = Solution()
    itenary = sol.findItinerary(input)
    print(itenary)

if __name__ == "__main__":
    test2()
