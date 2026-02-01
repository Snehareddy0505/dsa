class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        total=(n*(n+1))//2
        s2=0
        for i in range(0,n):
            s2 += nums[i]
        return total-s2
nums=[0,2,3,1,4]
sol=Solution()
print("resulting array is:",sol.missingNumber(nums)) 