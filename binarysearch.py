def binary_search(arr,target):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            low=mid-1
        else:
            high=mid+1
    return -1
arr=list(map(int,input().split()))
target=int(input())
print(binary_search(arr,target))