# LEAKY BUCKET

- The ```LeakyBucket``` class has a constructor (```__init__```) that initializes the bucket with a certain capacity, leak rate, and initially empty.
- The ```try_pour``` method attempts to pour a specified quantity of water into the bucket, returning True if successful and False if it would cause the bucket to overflow.
- The ```leak_water``` method is a helper method that "leaks" water from the bucket at the specified leak rate, based on the amount of time that has passed since the last leak.
