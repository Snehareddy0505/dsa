def ceil(arr, n, x):
    ans = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return arr[mid]  # exact match is the floor
        elif arr[mid] > x:
            ans = arr[mid]   # potential floor
            high= mid - 1
        else:
            low= mid + 1
    return ans
arr=[1,2,6,8]
print("result is:",ceil(arr,len(arr),5))