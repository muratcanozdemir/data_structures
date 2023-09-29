import time

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity  # Maximum burst rate
        self.leak_rate = leak_rate  # Leak rate per second
        self.water = 0  # Current water in the bucket
        self.last_leak_time = time.time()

    def try_pour(self, quantity):
        current_time = time.time()
        self.leak_water(current_time)
        if self.water + quantity <= self.capacity:
            self.water += quantity
            return True  # The water was poured into the bucket
        else:
            return False  # The bucket is full, water (request) is discarded

    def leak_water(self, current_time):
        # Determine the amount of time since the last leak
        delta_time = current_time - self.last_leak_time
        # Leak the appropriate amount of water from the bucket
        self.water = max(self.water - self.leak_rate * delta_time, 0)
        self.last_leak_time = current_time

# Usage:
# bucket = LeakyBucket(10, 1)  # Capacity of 10 units, leak rate of 1 unit per second
# if bucket.try_pour(5):
#     print("Poured 5 units into the bucket")
# else:
#     print("Failed to pour 5 units into the bucket")
