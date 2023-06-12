# Code Challenge: Class 16 
Find the Maximum Value in a Binary Tree

## Whiteboard Process
![](./assets/cc16.png)
## Approach & Efficiency
Approach: The function uses breadth-first traversal to iterate over the nodes of a binary tree and find the maximum value.

Efficiency: The efficiency depends on the efficiency of the breadth-first traversal and the max function. The breadth-first traversal has a time complexity of O(n) if it efficiently generates nodes one at a time, or O(n) space complexity if it requires storing the entire tree. The max function has a time complexity of O(n) and a space complexity of O(1). Therefore, the overall time complexity is O(n), and the space complexity is O(n) or O(1) depending on the implementation of the breadth-first traversal.
## Solution
```
    def tree_max(self):
        """
        Find the Maximum Value in a Binary Tree

        Args:
            no Args required

        Returns:
            number with the maximum value
        """

        return max(self.breadth_first())
```