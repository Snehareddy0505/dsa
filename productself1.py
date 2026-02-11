class Solution:
    def productExceptSelf(self,nums):
        n=len(nums)
        pref=[0]*n
        suff=[0]*n
        ans=[0]*n 
        pref[0]=nums[0]
        for i in range(1,n):
            pref[i]=pref[i-1]*nums[i]
        suff[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suff[i]=suff[i+1]*nums[i]
        ans[0]=suff[1]
        ans[n-1]=pref[n-2]
        for i in range(1,n-1):
            ans[i]=pref[i-1]*suff[i+1]
        return ans
nums=[1,2,3,4]
sol=Solution()
print("result is:",sol.productExceptSelf(nums))
      