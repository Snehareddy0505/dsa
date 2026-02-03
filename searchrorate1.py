class Solution:
 def rotatedarray(self,arr,target):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        if arr[low]<=mid:
            if arr[low]<=target and target<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=target and target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1
arr=[6,7,8,1,2,3,4,5]
sol=Solution()
print("resultis:",sol.rotatedarray(arr,2))