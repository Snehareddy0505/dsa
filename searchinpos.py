def searchinpos(arr,target,n):
    n=len(arr)
    ans = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
arr=[1,2,3,5,6,9]
print("result is:",searchinpos(arr,4,len(arr)))
