# Code Challenge: Class 38  - graph-depth-first
Implement a "Depth first" method in the Graph class for conducting a depth-first pre-order traversal. Provide a starting node as input, and the method returns a collection of nodes in the traversal order. Display this collection as the program's output.

## Whiteboard Process
![](./cc%2038.png)

## Approach & Efficiency
**Time Complexity:**
The time complexity is O(V * E) or O(n^2) because each vertex and edge is visited at most once during traversal in nested loop. 

**Space Complexity:**
The space complexity is O(V) due to memory usage for storing output, visited nodes, and the traversal stack.

## Solution
Here is the code and it passes all the tests.

```
 def depth_first(self, node=None):
        if node is None:
            return []
        output = []
        visited = set()
        stack = []
        start_vertex = node
        stack.append(start_vertex)
        visited.add(start_vertex)
        while len(stack):
            current_vertex = stack.pop()
            output.append(current_vertex.value)
            neighbors = self.get_neighbors(current_vertex)
            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        return output
```
