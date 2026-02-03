class Solution:
    def sortedarray(self,nums):
        for i in range(1,len(nums)):
           if nums[i] < nums[i-1]:
              return False
        return True
arr=[1,2,2,4]
sol=Solution()
print(sol.sortedarray(arr))