# Challenge Title
write a fuction to Find the first repeated word in a string in python using hashmap 
## Whiteboard Process
![](./ccccc.png)

## Approach & Efficiency
    Time Complexity: The time complexity of the function is O(N), where N is the length of the input string. The loop runs through the entire string once.

    
    Space Complexity: The space complexity is also O(N) because the function uses a hash table to store words. In the worst case, all words are unique and will be stored in the hash table.

## Solution

```
def repeated_word (in_srting):
    '''
    args : string
    Returns the first repeated word in a string
    '''
    hashtable = HashTable() 
    temp = ""
    word = ""
    pattern = r"[^\w\s]"
    srting = re.sub(pattern, "", in_srting)

    for i in range(len(srting) - 1,-1,-1):
                
        if(srting[i] != ' '):
            temp += srting[i]
        
        else:
                        
            if(hashtable.has(temp)):
                word = temp
            else:
                hashtable.set(temp,1)
            
            temp = ""
            
    if(hashtable.has(temp)):
        word=temp
                        
    if(word!=""):

        word = word[::-1]
        return word
    else:
        return "No Repetition"
```

