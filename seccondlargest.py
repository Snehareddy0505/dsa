class Solution:
    def largestelement(self,nums):
            largestelement=nums[0]
            for i in range(1,len(arr)):
               if nums[i]>largestelement:
                largestelement=nums[i]
            return largestelement

    def seclargestelement(self,nums):
        largestelement=self.largestelement(nums)
        seclargestelement=-1
        for i in range(0,len(nums)):
            if nums[i] !=largestelement and nums[i]>seclargestelement:
                seclargestelement=nums[i]
        return seclargestelement
arr=[1,2,5,4,7,3,8]
sol=Solution()
print("secondlargest is:",sol.seclargestelement(arr))