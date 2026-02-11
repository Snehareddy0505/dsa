class Solution:
    def productExceptSelf(self,nums):
        n=len(nums)
        ans=[1]*n
        pref=1
        for i in range(n):
            ans[i]=pref
            pref*=nums[i]
        suff=1
        for i in range(n-1,-1,-1):
            ans[i]*=suff
            suff*=nums[i]
        return ans
nums=[1,2,3,4]
sol=Solution()
print("result is:",sol.productExceptSelf(nums))