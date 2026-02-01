class Solution:
    def leaders(self, nums):
        n=len(nums)
        result=[]
        for i in range(n):
            leader=True
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    leader=False
                    break
            if leader:
                result.append(nums[i])
        return result
arr=[1,2,5,3,1,2]
sol=Solution()
print("leader is:",sol.leaders(arr)) 