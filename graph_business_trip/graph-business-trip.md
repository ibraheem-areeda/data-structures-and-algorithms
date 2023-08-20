# Code Challenge: Class 37 - graph-business-trip
Create a function called "business trip" that takes a graph of city connections and an array of city names as input. The function should determine if a direct flight route exists for the given cities and return the cost if possible, or null if not. It essentially calculates the travel cost for the trip based on direct flights, if available.

## Whiteboard Process
![](./cc%2037.png)

## Approach & Efficiency
**Time Complexity:**
The time complexity of the code is O(n * m) or O(n^2), where:
- `n` is the number of cities in the `arr_cities` array.
- `m` is the maximum number of neighbors for a city in the graph.

**Space Complexity:**
The space complexity of the code is O(1), as it doesn't use additional space that grows with the input size. The primary variable affecting space complexity is `cost`, and no additional data structures are created that depend on the input size.

## Solution
Here is the code and it passes all the tests.

```
def business_trip(graph, arr_cities):
    cost = 0
    if len(arr_cities) == 0:
        return None
    for city in range(len(arr_cities) - 1):
        for neighbor in graph.get_neighbors(arr_cities[city]):
            if neighbor.vertix == arr_cities[city + 1]:
                cost += neighbor.weight
                print(neighbor)
    if cost == 0:
        return 'Null'
    else:
        return f"${cost}"
```
