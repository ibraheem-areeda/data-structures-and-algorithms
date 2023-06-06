# stack_queue_brackets
The code challenge is to implement a function called "validate_brackets" that takes a string as input and determines whether the brackets in the string are balanced. The function should return a boolean value indicating whether the brackets are balanced or not. The brackets to consider are round brackets (), square brackets [], and curly brackets {}.
## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
The code implements a function called "validate_brackets" to check if the brackets in a given string are balanced. It follows a simple approach of removing non-bracket characters from the string and then iteratively checking for valid pairs of brackets. The code uses two queues to store the brackets, dequeues them when valid pairs are found, and checks for error cases such as unmatched opening or closing brackets. Finally, it returns True if all brackets are balanced, and False otherwise. The time and space complexity of the code are both O(n), where n is the length of the input string.

The time complexity of this approach is O(n), where n is the length of the input string. The code iterates over the string once, enqueues and dequeues brackets, and performs some string operations. The space complexity is also O(n) because the two queues can store up to n/2 brackets each.
## Solution
```
def validate_brackets (string):
    queue1 = Queue()
    queue2 = Queue()
    validation_arr = ["{}","()","[]"]
    empty_brackets = re.sub(r"[^\]\[\(\)\{\}]+", "" , string ) # remove extra characters 

    if len(empty_brackets) and empty_brackets in ["(","[","{"] : 
        print (f"error unmatched opening {empty_brackets} remaining.")  # handel unmatched opening
        return False
    if len(empty_brackets) and empty_brackets in [")","]","}"] :
        print (f"error closing {empty_brackets} arrived without corresponding opening")  # handel closing without corresponding opening
        return False
    if len(empty_brackets) % 2 != 0 :return False   # check if the string is odd 
    if len(empty_brackets) == 2 and empty_brackets[0] + empty_brackets [1] not in validation_arr : 
        print(f"error closing {empty_brackets[1]}. Doesn’t match opening {empty_brackets[0]}.")   # handel one bracket open close case
        return False
    for bracket in range(len(empty_brackets)):
        queue1.enqueue(empty_brackets[bracket])   # enqueue the srting into the queue1
    queue1.dequeue()  

    while queue1.front :
        if empty_brackets[0]+ queue1.front.value in  validation_arr :
            queue1.dequeue()
            if queue1.front :
                empty_brackets = queue1.front.value
                queue1.dequeue()
            else:
                return True   # return True when the queue1 is empty 
        else:
            test = queue1.to_string()
            if len(test)>=3 and test[0] + test[2] in validation_arr and test[0] != test[1] and test[2] != test[1]:
                return False        # to handel the alternated open cloese case
            temp = queue1.front
            queue1.dequeue()
            queue2.enqueue(temp)     # to save the unmatched brakcets in queue2

    while queue2.front:
        temp = queue2.front
        queue2.dequeue()
        queue1.enqueue(temp)        # to return the unmatched brakcets to queue1

    while queue1.front :
        if str(queue1.front.value) + empty_brackets[0] in validation_arr :      # apply the same logc befor but in backwords
            queue1.dequeue()
            if queue1.front :
                empty_brackets = queue1.front.value
                queue1.dequeue()
            else:
                    return True      # return True when the queue1 is empty 
```
