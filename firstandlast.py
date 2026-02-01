def lowerbound(arr, target):
    n = len(arr)
    ans = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def upperbound(arr, target):
    n = len(arr)
    ans = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def find_first_and_last_position(arr, k):
    lb = lowerbound(arr, k)
    if lb == len(arr) or arr[lb] != k:
        return [-1, -1]
    ub = upperbound(arr, k)
    return [lb, ub - 1]
arr = [1, 2, 2, 2, 3, 4, 5]
k = 2
print(find_first_and_last_position(arr, k))  
