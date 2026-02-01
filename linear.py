class Solution:
    def linearSearch(self, nums, target):
        target=5
        for i in range(0,len(nums)):
            if nums[i]==target:
                return nums[i]
        return -1
nums=[2,3,4,5,3]
sol=Solution()
print("resulting array is:",sol.linearSearch(nums,6))