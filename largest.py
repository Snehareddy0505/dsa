class Solution:
    def largestElement(self, nums):
        largestElement=nums[0]
        for i in range(1,len(nums)):
           if nums[i]>largestElement:
               largestElement=nums[i]
        return largestElement
arr=[3,3,5,1]
sol=Solution()
print("largest element is:",sol.largestElement(arr))
