# array-reverse
I will write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available in python, it will return an array with elements in reversed order.

## Whiteboard Process
![](./assets/code%20challange%201.png)

## Approach & Efficiency
What approach did you take? 
I used the slice notation [::-1] to create a reversed copy of the original array, which is assigned to the variable reversed_array. Then, the reversed array is printed to the console using the print() function.

## Solution

def reverseArray(arr):
    reversed_array = arr[::-1]
    return reversed_array