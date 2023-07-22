# Sorting: Comparisons

I used insertion sort for sorting the years and the title string 

## efficiency
The efficiency of the Insertion Sort algorithm can be analyzed in terms of its time complexity and space complexity.

Time Complexity:
- Worst case: O(n^2) when the input array is in reverse sorted order. In the worst case, the algorithm requires n-1 comparisons and shifts for each element, resulting in a quadratic time complexity.

Space Complexity:
- The space complexity of the Insertion Sort algorithm is O(1) because it performs in-place sorting. It does not require any additional space proportional to the input size.


```
def sort_movies_obj_yearly (arr):

    for i in range(1, len(arr)):
        key = arr[i]['year']
        print(key)
        j = i - 1
        while j >= 0 and arr[j]['year'] > key:
            arr[j + 1]['year'] = arr[j]['year']
            j -= 1
        arr[j + 1]['year'] = key
    return arr
    
def sort_movies_obj_alphabetical (arr):
    

    for i in range(1, len(arr)):
            
        if arr[i]["title"].startswith(( "a", "an")):
            arr[i]["title"] = arr[i]["title"][3:]
        
        if arr[i]["title"].startswith("the"):
            arr[i]["title"] = arr[i]["title"][4:]

    
        key = arr[i]['title']
        print(key)
        j = i - 1
        while j >= 0 and arr[j]['title'] > key:
            arr[j + 1]['title'] = arr[j]['title']
            j -= 1
        arr[j + 1]['title'] = key
    return arr
```