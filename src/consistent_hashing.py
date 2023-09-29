import hashlib

class ConsistentHashing:
    def __init__(self, nodes=None):
        self.nodes = nodes or {}
        self.ring = {}
        self._sorted_keys = []

        for node in self.nodes:
            self.add_node(node)

    def add_node(self, node):
        key = self._hash(node)
        self.ring[key] = node
        self._sorted_keys = sorted(self.ring.keys())

    def remove_node(self, node):
        key = self._hash(node)
        del self.ring[key]
        self._sorted_keys = sorted(self.ring.keys())

    def get_node(self, string_key):
        if not self.ring:
            return None

        key = self._hash(string_key)
        nodes = self._sorted_keys
        for node_key in nodes:
            if key <= node_key:
                return self.ring[node_key]

        return self.ring[nodes[0]]

    def _hash(self, key):
        """Generate a hash for the given key"""
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

# Usage:
# nodes = ['node1', 'node2', 'node3']
# ch = ConsistentHashing(nodes)
# print(ch.get_node('some_key'))  # Output: nodeX based on the hash of 'some_key'
