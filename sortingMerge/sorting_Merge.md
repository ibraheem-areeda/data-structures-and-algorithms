# sorting-merge

this table to illustrate the changes in the `arr` list during each, the given input `[8, 4, 23, 42, 16, 15]`:

| Iteration | `arr`           | `left` | `right` |
|-----------|-----------------|--------|---------|
| Initial   | [8, 4, 23, 42, 16, 15] |        |         |
| 1         | [8, 4, 23]      | [8]    | [4, 23] |
| 2         | [8]             |        |         |
| 3         | [4, 23]         | [4]    | [23]    |
| 4         | [23]            |        |         |
| Merge 3-4 | [4, 23]         | [4]    | [23]    |
| 5         | [42, 16, 15]    | [42]   | [16, 15]|
| 6         | [42]            |        |         |
| 7         | [16, 15]        | [16]   | [15]    |
| 8         | [16]            |        |         |
| Merge 7-8 | [15, 16]        | [16]   | [15]    |
| Merge 5-8 | [15, 16, 42]    | [42]   | [15, 16]|
| Merge 1-4 | [4, 8, 23, 42]  | [8]    | [4, 23] |
| Final     | [4, 8, 15, 16, 23, 42] |        |         |

In each iteration, the `arr` list is updated according to the merge sort algorithm until the final sorted list is obtained. The `left` and `right` columns show the partitioned sub-arrays at each iteration. The "Merge" rows represent the merging of the sub-arrays back into the original `arr` list.
 
## efficiency
The efficiency of the merge sort algorithm can be analyzed in terms of time complexity and space complexity.

Time Complexity:
Merge sort has a time complexity of O(n log n) in the average and worst cases. This means that as the size of the input array (n) increases, the time it takes to sort the array grows in a logarithmic manner. The recursive nature of merge sort divides the array into smaller sub-arrays, and the merging process combines them in sorted order. The overall time complexity is determined by the number of comparisons and merges performed, which is proportional to n log n.

Space Complexity:
The space complexity of merge sort is O(n) in the worst case. This is because merge sort requires additional memory to store the divided sub-arrays during the recursive calls. In each recursive call, the original array is divided into two halves until the base case is reached. This division requires additional space to store the sub-arrays. However, merge sort does not create new arrays for each partition, but rather uses the same input array by dividing it into smaller parts. Hence, the total auxiliary space used is proportional to the size of the input array, resulting in a space complexity of O(n).


```
def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)


def merge(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

```