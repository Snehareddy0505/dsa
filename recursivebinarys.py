class Solution:
    def recursivebinarysearch(self,arr,low,high,target):
        if low>high:
            return -1
        mid=(low+high) //2
        if arr[mid]==target: 
            return mid
        elif target> arr[mid]:
            return self.recursivebinarysearch(arr,mid+1,high,target)
        return self.recursivebinarysearch(arr,low,mid-1,target)
arr=[1,2,3,4,5,6,9]
sol=Solution()
print("result is:",sol.recursivebinarysearch(arr,0,len(arr)-1,6))
