#Merge Sort Basic
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left_half, right_half):
    sorted_arr = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1

        else:
            sorted_arr.append(right_half[j])
            j += 1

    sorted_arr.extend(left_half[i:])
    sorted_arr.extend(right_half[j:])
    return sorted_arr

arr = [38, 2, 43, 12, 5]
print(merge_sort(arr))



#Merge sort count
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr)//2
    left_half, left_count = merge_sort(arr[:mid])
    right_half, right_count = merge_sort(arr[mid:])

    merged, merge_count = merge(left_half, right_half)
    total_count = left_count + right_count + merge_count
    return merged, total_count

def merge(left_half, right_half):
    sorted_arr = []
    i = 0
    j = 0
    count = 0

    while i < len(left_half) and j < len(right_half):
        count += 1
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1

        else:
            sorted_arr.append(right_half[j])
            j += 1

    sorted_arr.extend(left_half[i:])
    sorted_arr.extend(right_half[j:])
    return sorted_arr, count

arr = [5, 3, 8, 1, 9, 2, 7, 4]
sorted, count = merge_sort(arr)
print("Sorted: ", sorted)
print("Total Comparisons: ", count)