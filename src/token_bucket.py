import time

class TokenBucket:
    def __init__(self, capacity, fill_rate):
        self.capacity = capacity  # Maximum number of tokens in the bucket
        self.fill_rate = fill_rate  # Rate at which tokens are added per second
        self.tokens = capacity  # Initially, bucket is full
        self.last_fill_time = time.time()

    def try_consume(self, tokens):
        current_time = time.time()
        self.refill_tokens(current_time)
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True  # Tokens were consumed
        else:
            return False  # Not enough tokens

    def refill_tokens(self, current_time):
        if self.tokens < self.capacity:
            delta_time = current_time - self.last_fill_time
            refill_amount = self.fill_rate * delta_time
            self.tokens = min(self.tokens + refill_amount, self.capacity)
            self.last_fill_time = current_time

# Usage:
# bucket = TokenBucket(10, 1)  # Capacity of 10 tokens, fill rate of 1 token per second

# if bucket.try_consume(5):
#     print("Consumed 5 tokens")
# else:
#     print("Failed to consume 5 tokens")
