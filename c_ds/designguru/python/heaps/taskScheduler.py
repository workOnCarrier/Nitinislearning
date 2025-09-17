import heapq
import time
from collections import deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = [0]*26
        for task in tasks :
            offset = ord(task) - ord('A')
            freq[offset] += 1
        pq = [(-freq, task) for task, freq in enumerate(freq) if freq != 0 ]
        heapq.heapify(pq)
        processed = deque()
        steps = 0
        while pq :
            scheduled_task = False
            for _ in range(n+1):
                if pq:
                    candidate = heapq.heappop(pq)
                    if candidate[0] + 1 != 0:
                        processed.append((candidate[0]+1, candidate[1]))
                steps += 1
                if not processed:
                    break
            for _ in range(len(processed)):
                heapq.heappush(pq, processed.popleft())
        return steps

def test():
    tasks, cycle_len = ['A', 'B', 'C', 'A', 'A', 'B', 'B'], 3
    # tasks, cycle_len = ["B","C","D","A","A","A","A","G"], 1
    # tasks, cycle_len = ["A","A","A","B","B","B"], 2

    s = Solution()
    print(f"\t tasks:{tasks} \t cycle:{cycle_len}")
    intervals = s.leastInterval(tasks, cycle_len)
    print(f"\t intervals:{intervals}")


if __name__ == "__main__":
    test()