'''#Bubble sort basic
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [29, 10, 14, 37, 13]
print(bubble_sort(arr))



#Selection sort basic
def Selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [64, 25, 12, 22, 11]
print(Selection_sort(arr))



#Count swaps in bubble sort
def bubble_sort(arr):
    n = len(arr)
    total_swaps = 0

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                total_swaps += 1

    return arr, total_swaps

arr = [5, 3, 8, 1, 9, 2]
sorted_arr, swaps = bubble_sort(arr)
print("Sorted Array:", sorted_arr)
print("Total Swaps:", swaps)
'''