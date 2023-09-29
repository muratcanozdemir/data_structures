# QUADTREE

- We create a Node class to represent the points in our Quadtree.
- We create a Quadtree class with methods to insert nodes, subdivide the Quadtree, and check if a point is contained within a Quadtree node.
- The insert method adds a point to the Quadtree. If the current Quadtree node exceeds its capacity, it subdivides into four child Quadtrees (if it hasn't already) and redistributes the points.
- The subdivide method creates four child Quadtrees representing the northwest, northeast, southwest, and southeast quadrants.
- The _insert_into_subtree and _contains methods are helper methods to recursively insert nodes into the appropriate child Quadtrees and to check if a point is contained within a Quadtree node's bounds, respectively.