import heapq

class JobScheduler:
    def __init__(self):
        self.min_heap = []      # stores (time, job_id)
        self.canceled = set()   # stores canceled job_ids

    def schedule(self, time: int, job_id: int) -> None:
        """Schedules a job with ID job_id to execute at the designated time."""
        heapq.heappush(self.min_heap, (time, job_id))

    def cancel(self, job_id: int) -> None:
        """Cancels the job with the specified ID."""
        self.canceled.add(job_id)

    def run(self, time: int) -> list[int]:
        """
        Returns all job IDs (in order) scheduled for or before a given time,
        excluding canceled jobs.
        """
        result = []
        while self.min_heap and self.min_heap[0][0] <= time:
            t, job_id = heapq.heappop(self.min_heap)
            if job_id in self.canceled:
                self.canceled.remove(job_id)  # cleanup lazy delete
                continue
            result.append(job_id)
        return result


def main():
    sched = JobScheduler()

    sched.schedule(5, 101)
    sched.schedule(3, 102)
    sched.schedule(7, 103)

    sched.cancel(102)

    print(sched.run(4))   # []   (102 was canceled, nothing left <=4)
    print(sched.run(5))   # [101]
    print(sched.run(10))  # [103]

if __name__ == "__main__":
    main()