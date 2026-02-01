class Solution:
    def leftrotateArray(self,nums,k):
        n=len(nums)
        k=k%n
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])
        nums[:]=reversed(nums)
        return nums
arr=[1,2,3,4,5,6,7]
sol=Solution()
print("resulting arrayis:",sol.leftrotateArray(arr,3))