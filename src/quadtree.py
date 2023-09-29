class Node:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
        self.NW = None
        self.NE = None
        self.SW = None
        self.SE = None

class Quadtree:
    def __init__(self, capacity, x_range, y_range):
        self.capacity = capacity
        self.x_range = x_range
        self.y_range = y_range
        self.points = []
        self.divided = False

    def insert(self, node):
        if len(self.points) < self.capacity:
            self.points.append(node)
        else:
            if not self.divided:
                self.subdivide()
            self._insert_into_subtree(node)

    def subdivide(self):
        x_mid = (self.x_range[0] + self.x_range[1]) / 2
        y_mid = (self.y_range[0] + self.y_range[1]) / 2
        
        self.NW = Quadtree(self.capacity, (self.x_range[0], x_mid), (y_mid, self.y_range[1]))
        self.NE = Quadtree(self.capacity, (x_mid, self.x_range[1]), (y_mid, self.y_range[1]))
        self.SW = Quadtree(self.capacity, (self.x_range[0], x_mid), (self.y_range[0], y_mid))
        self.SE = Quadtree(self.capacity, (x_mid, self.x_range[1]), (self.y_range[0], y_mid))
        
        for point in self.points:
            self._insert_into_subtree(point)
        self.points = []
        self.divided = True
        
    def _insert_into_subtree(self, node):
        if self.NW._contains(node):
            self.NW.insert(node)
        elif self.NE._contains(node):
            self.NE.insert(node)
        elif self.SW._contains(node):
            self.SW.insert(node)
        elif self.SE._contains(node):
            self.SE.insert(node)

    def _contains(self, node):
        return self.x_range[0] <= node.x < self.x_range[1] and self.y_range[0] <= node.y < self.y_range[1]

# Usage:
# quadtree = Quadtree(capacity=4, x_range=(0, 100), y_range=(0, 100))
# points = [(10, 10, 'a'), (20, 20, 'b'), (30, 30, 'c'), (40, 40, 'd'), (50, 50, 'e')]

# for point in points:
#     quadtree.insert(Node(*point))
