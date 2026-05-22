#Find Minimum in Rotated Array
arrays = [
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [4, 5, 6, 7, 0, 1, 2],
    [1, 2, 3, 4, 5],   # not rotated
    [3, 1],
    [1]                 # single element
]

def find_min_rotated(arr):
    left = 0
    right = len(arr) - 1
    steps = 0

    if arr[left] <= arr[right]:
        return arr[left], left, 1

    while left < right:
        steps += 1
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            left = mid + 1

        else:
            right = mid

    return arr[left], left, steps
for i, arr in enumerate(arrays, start = 1):
   minimum, index, steps = find_min_rotated(arr)
   print(f"Array {i}, Minimum: {minimum}, Index: {index}, Steps: {steps}")