#Binary Search Basic + steps taken
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, steps
        
        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1

    return -1, steps

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search(arr, 23))
print(binary_search(arr, 2))
print(binary_search(arr, 91))
print(binary_search(arr, 50))


#First and Last Position of Element in Sorted Array
def find_first(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result

def find_last(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

def find_first_last(arr, target):
    first = find_first(arr, target)

    if first == -1:
        return [-1, -1]
    
    last = find_last(arr, target)
    return [first, last]

arr     = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
print(find_first_last(arr, 2))
print(find_first_last(arr, 3))
print(find_first_last(arr, 4))
print(find_first_last(arr, 6))
