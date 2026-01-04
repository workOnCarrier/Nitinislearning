from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        level, mrow, mcol = 0, len(grid), len(grid[0])
        subm, qued = set(), set()
        pq = [(grid[0][0], 0,0)]
        qued.add( (0,0) )
        isvalid = lambda x, y: (x < mrow and x >= 0 and y < mcol and y >= 0 and 
                                (x,y) not in qued and (x,y) not in subm )
        while pq:
            print(f"\t pq: {pq}")
            print(f"\t qued: {qued}")
            cur, x, y = heapq.heappop(pq)
            qued.remove( (x,y) )
            subm.add( (x, y) )
            level = max(level, cur)
            if x == mrow -1 and y == mrow -1 :
                level = max(level, cur)
                break
            neis = [ (x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            valneis = [ (x,y) for x, y in neis if isvalid(x,y)]
            for nx, ny in valneis:
                qued.add( (nx, ny) )
                heapq.heappush(pq,  (grid[nx][ny], nx, ny) )
        return level
        
def test():
    input = grid=[[0,1],[2,3]]

    expected = 3
    s = Solution()
    time = s.swimInWater(input)
    print(f"\t expected: {expected}  --- v/s --- {time}")

if __name__ == "__main__":
    test()