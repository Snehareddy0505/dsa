class Solution:
    def rearrangeArray(self, nums):
        posindex=0
        negindex=1
        ans=[0]*len(nums)
        n=len(nums)
        for i in range(0,n):
            if nums[i]<0:
                ans[negindex]=nums[i]
                negindex+=2
            else:
                ans[posindex]=nums[i]
                posindex+=2
        return ans
arr=[2,4,5,-1,-3,-4]
sol=Solution()
print("result is:",sol.rearrangeArray(arr))