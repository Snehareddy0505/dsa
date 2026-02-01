class Solution:
    def leaders(self, nums):
        n=len(nums)
        ans=[]
        maxi=float('-inf')
        for i in range(n-1,-1,-1):
            if nums[i]>maxi:
                ans.append(nums[i])
            maxi=max(maxi,nums[i])
        ans.sort()
        return ans
arr=[1,2,5,3,1,2]
sol=Solution()
print("leader is:",sol.leaders(arr)) 