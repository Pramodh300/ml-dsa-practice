#Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        if arr[j] < pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    pivot_index = i + 1

    print(f"After partition: {arr}  "
          f"pivot={pivot} at index {pivot_index}")

    return pivot_index


def quick_sort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)

        quick_sort(arr, pi + 1, high)


# Test
arr = [29, 10, 14, 37, 13]

quick_sort(arr, 0, len(arr) - 1)

print("Final:", arr)


#Quick Sort with Count
# Quick Sort + Count Comparisons

def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    comparisons = 0

    for j in range(low, high):

        # Count comparison
        comparisons += 1

        if arr[j] < pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot correctly
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1, comparisons


def quick_sort(arr, low, high):

    total_comparisons = 0

    if low < high:

        # Partition
        pivot_index, comparisons = partition(
            arr, low, high
        )

        total_comparisons += comparisons

        # Left recursion
        total_comparisons += quick_sort(
            arr,
            low,
            pivot_index - 1
        )

        # Right recursion
        total_comparisons += quick_sort(
            arr,
            pivot_index + 1,
            high
        )

    return total_comparisons


# Test
arr = [64, 34, 25, 12, 22, 11, 90]

count = quick_sort(arr, 0, len(arr) - 1)

print("Sorted:", arr)

print("Total comparisons:", count)