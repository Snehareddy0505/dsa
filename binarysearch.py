class Solution:
    def binarysearch(self,arr,n,target):
        n=len(arr)
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high) // 2
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
arr=[1,2,3,4,5,6,9]
sol=Solution()
print("result is:",sol.binarysearch(arr,len(arr),6))

   