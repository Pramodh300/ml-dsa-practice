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


#Search in 2D Matrix
matrix1 = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

matrix2 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

targets1 = [3, 16, 60, 25]
targets2 = [5, 20, 30, 100]


# -----------------------------------
# MATRIX 1 → Binary Search
# -----------------------------------

def search_matrix1(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    steps = 0

    while left <= right:

        steps += 1

        mid = (left + right) // 2

        row = mid // cols
        col = mid % cols

        value = matrix[row][col]

        if value == target:
            return True, row, col, steps

        elif value < target:
            left = mid + 1

        else:
            right = mid - 1

    return False, -1, -1, steps


# -----------------------------------
# MATRIX 2 → Staircase Search
# -----------------------------------

def search_matrix2(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    steps = 0

    while row < rows and col >= 0:

        steps += 1

        value = matrix[row][col]

        if value == target:
            return True, row, col, steps

        elif value > target:
            col -= 1

        else:
            row += 1

    return False, -1, -1, steps


# -----------------------------------
# SEARCH MATRIX 1
# -----------------------------------

print("MATRIX 1 RESULTS:\n")

for target in targets1:

    found, row, col, steps = search_matrix1(matrix1, target)

    if found:
        print(
            f"Matrix1, Target {target}: "
            f"Found at row={row}, col={col}, "
            f"steps={steps}"
        )

    else:
        print(
            f"Matrix1, Target {target}: "
            f"Not Found, steps={steps}"
        )


# -----------------------------------
# SEARCH MATRIX 2
# -----------------------------------

print("\nMATRIX 2 RESULTS:\n")

for target in targets2:

    found, row, col, steps = search_matrix2(matrix2, target)

    if found:
        print(
            f"Matrix2, Target {target}: "
            f"Found at row={row}, col={col}, "
            f"steps={steps}"
        )

    else:
        print(
            f"Matrix2, Target {target}: "
            f"Not Found, steps={steps}"
        )