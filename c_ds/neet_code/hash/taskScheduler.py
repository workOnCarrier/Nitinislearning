from collections import deque, defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: list, n: int) -> int:
        counter = defaultdict(int)
        for t in tasks:
            counter[t] += 1
        mh = [-fr for fr in counter.values()]
        heapq.heapify(mh)
        q = deque()
        time = 0
        while mh or q:
            time += 1
            if not mh:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(mh)
                if count != 0:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(mh, q.popleft()[0])
        return time


def test():
    s = Solution()
    input = ["A","A","A","B","B","B"]
    time = s.leastInterval(input, 2)
    print(f"Time taken : {time}")

if __name__ == "__main__":
    test()
