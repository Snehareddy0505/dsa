class Solution:
    def maxSubArray(self, nums):
         n=len(nums)
         sum=0
         maxi=float('-inf')
         for i in range(0,n):
              sum+=nums[i]
              if sum>maxi:
                   maxi=sum
              if sum<0:
                   sum==0
         return maxi
arr=[2,3,5,-2,7,-4]
sol=Solution()
print("result is:",sol.maxSubArray(arr)) 
                   