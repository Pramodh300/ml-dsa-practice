'''#Binary search on rotated array
def binary_rotated(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, "Found at index: " + str(mid)
        
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1

            else:
                low = mid + 1

        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1

arr1 = [6, 7, 8, 9, 1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 0, 1, 2]
arr3 = [3, 1]

print(binary_rotated(arr1, 9))
print(binary_rotated(arr2, 0))
print(binary_rotated(arr3, 1))
'''


#Search in Rotated Array + Count Steps
# Search in Rotated Array + Count Steps

def search_rotated(arr, target):

    low = 0
    high = len(arr) - 1

    steps = 0

    print(f"\nTarget {target}:")

    while low <= high:

        steps += 1

        mid = (low + high) // 2

        print(f"  Step {steps}: mid={mid}(val={arr[mid]})")

        # Found target
        if arr[mid] == target:

            print(f"  FOUND at index {mid}!")
            print(f"  Steps taken: {steps}")

            return mid

        # Left half sorted
        if arr[low] <= arr[mid]:

            print("    Left half is sorted")

            # Target inside left half
            if arr[low] <= target < arr[mid]:

                print(f"    Search LEFT, high={mid - 1}")

                high = mid - 1

            else:

                print(f"    Search RIGHT, low={mid + 1}")

                low = mid + 1

        # Right half sorted
        else:

            print("    Right half is sorted")

            # Target inside right half
            if arr[mid] < target <= arr[high]:

                print(f"    Search RIGHT, low={mid + 1}")

                low = mid + 1

            else:

                print(f"    Search LEFT, high={mid - 1}")

                high = mid - 1

    print(f"  Not Found, steps taken: {steps}")

    return -1


arr = [15, 18, 20, 25, 1, 3, 6, 9, 12]

targets = [20, 3, 25, 7]

for t in targets:
    search_rotated(arr, t)


#Find Pivot in Rotated Array
# Find Pivot in Rotated Array

def find_pivot(arr):

    low = 0
    high = len(arr) - 1

    # Array not rotated
    if arr[low] <= arr[high]:
        return 0

    while low <= high:

        mid = (low + high) // 2

        # Check if mid is pivot
        if mid < high and arr[mid] > arr[mid + 1]:
            return mid + 1

        # Check if previous is pivot
        if mid > low and arr[mid] < arr[mid - 1]:
            return mid

        # Left half sorted → pivot on right
        if arr[low] <= arr[mid]:
            low = mid + 1

        # Right half sorted → pivot on left
        else:
            high = mid - 1

    return 0


arr1 = [7, 8, 9, 1, 2, 3, 4, 5, 6]
arr2 = [4, 5, 6, 7, 8, 1, 2, 3]
arr3 = [1, 2, 3, 4, 5]
arr4 = [2, 1]

arrays = [arr1, arr2, arr3, arr4]

for i, arr in enumerate(arrays, start=1):

    pivot = find_pivot(arr)

    if pivot == 0 and arr[0] <= arr[-1]:
        print(f"arr{i}: pivot at index 0 (not rotated)")

    else:
        print(f"arr{i}: pivot at index {pivot} (value={arr[pivot]})")