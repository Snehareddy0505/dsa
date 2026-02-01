class Solution:
    def majorityElement(self, nums):
     n=len(nums)
     for i in range(0,n):
        cnt=0
        for j in range(0,n):
            if nums[i]==nums[j]:
                cnt+=1
            if cnt>n/2:
                return nums[i]
     return -1
arr=[1,1,1,2,1,2]
sol=Solution()
print("result  is:",sol.majorityElement(arr))    