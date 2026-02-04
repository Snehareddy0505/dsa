class Solution:
    def twoSum(self, nums, target):
      n=len(nums)
      for i in range(0,n):
        for j in range(i+1,n):
            if i==j:
                continue
            if nums[i]+nums[j]==target:
                return "YES",(i,j)
      return "No",(-1,-1)
arr=[1,6,2,10,3]
sol=Solution()
result,indices=sol.twoSum(arr,8)
print("result:",result)
print("indices:",indices)