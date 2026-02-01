class Solution:
    def maxSubArray(self, nums):
       maxi=float('-inf')
       n=len(nums)
       for i in range(0,n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum+=nums[k]
                maxi=max(sum,maxi)
       return maxi
arr=[2,3,5,-2,7,-4]
sol=Solution()
print("result is:",sol.maxSubArray(arr)) 