class Solution:
    def twoSum(self,nums,target):
        nums.sort()
        left=0
        right=len(nums)-1
        while left < right:
            current_Sum=nums[left]+nums[right]
            if current_Sum==target:
                return"YES"
            elif  current_Sum<target:
                left+=1
            else:
                right-=1
        return "NO"
arr=[1,6,2,10,3]
sol=Solution()
print("result is:",sol.twoSum(arr,9)) 