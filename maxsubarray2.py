class Solution:
    def maxSubArray(self, nums):
        maxi=float('-inf')
        n=len(nums)
        for i in range(0,n):
            sum=0
            for j in range(i,n):
                sum+=arr[j]
                maxi=max(sum,maxi)
        return maxi
arr=[2,3,5,-2,7,-4]
sol=Solution()
print("result is:",sol.maxSubArray(arr)) 