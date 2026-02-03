def lower_bound(arr, target):
    low = 0
    high = len(arr) - 1
    ans = len(arr)  # Default: target not found, all elements are less than target

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

def row_with_max_1s(matrix):
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0

    max_ones = 0
    row_index = -1

    for i in range(n):
        first_one_index = lower_bound(matrix[i], 1)
        count_ones = m - first_one_index

        if count_ones > max_ones:
            max_ones = count_ones
            row_index = i

    return row_index
matrix = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]
]

print(row_with_max_1s(matrix))  
