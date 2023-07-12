
def insert(sorted_list, value):
    i = 0
    while value > sorted_list[i]:
        i += 1
    while i < len(sorted_list):
        temp = sorted_list[i]
        sorted_list[i] = value
        value = temp
        i += 1
    sorted_list.append(value)
    return sorted_list


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":

    arr = [5, 2, 9, 1, 7]
    insertion_sort(arr)
    print(arr)
    insert(arr,8)
    print(arr)
 
