class Solution:
    def rotateArray(self, nums, k):
        n=len(nums)
        k=nums[0]
        for i in range(1,len(arr)):
            nums[i-1]=nums[i]
        nums[n-1]=k
        return nums
arr=[1,2,3,4,5,6]
sol=Solution()
print("resulting array is:",sol.rotateArray(arr,1))