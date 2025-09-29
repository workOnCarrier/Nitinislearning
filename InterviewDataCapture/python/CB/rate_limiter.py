import time
from collections import defaultdict

class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate: float):
        """
        :param capacity: Maximum tokens per bucket (N)
        :param refill_rate: Number of tokens refilled per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        # Store user buckets as {user_id: (tokens, last_refill_time)}
        self.buckets = defaultdict(lambda: [capacity, time.time()])

    def allow_request(self, user_id: str) -> bool:
        """
        Check if a request is allowed for the given user_id.
        Implements lazy token refill.
        """
        tokens, last_time = self.buckets[user_id]
        now = time.time()

        # Calculate tokens to refill since last_time
        elapsed = now - last_time
        refill = elapsed * self.refill_rate
        tokens = min(self.capacity, tokens + refill)

        # Update bucket state
        if tokens >= 1:
            tokens -= 1
            self.buckets[user_id] = [tokens, now]
            return True  # Request allowed
        else:
            self.buckets[user_id] = [tokens, now]
            return False  # Request rejected


# Example usage
if __name__ == "__main__":
    limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1)  # 5 tokens max, 1 token/sec

    user = "alice"

    # Simulate requests
    for i in range(10):
        allowed = limiter.allow_request(user)
        print(f"Request {i+1}: {'Allowed ✅' if allowed else 'Blocked ❌'}")
        time.sleep(0.5)  # half a second between requests
