import hashlib

class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.hash_functions = hash_functions
        self.bit_array = 0  # Initialize all bits to 0

    def add(self, item):
        for hash_func in self.hash_functions:
            index = int(hash_func(item).hexdigest(), 16) % self.size
            self.bit_array |= (1 << index)  # Set the bit at index to 1

    def __contains__(self, item):
        for hash_func in self.hash_functions:
            index = int(hash_func(item).hexdigest(), 16) % self.size
            if not self.bit_array & (1 << index):  # Check if the bit at index is 0
                return False
        return True

# Define hash functions
def hash1(item):
    return hashlib.md5(item.encode('utf-8'))

def hash2(item):
    return hashlib.sha1(item.encode('utf-8'))

# Usage
# bloom_filter = BloomFilter(1000, [hash1, hash2])
# bloom_filter.add('example')
# print('example' in bloom_filter)  # Output: True
# print('test' in bloom_filter)     # Output: False
