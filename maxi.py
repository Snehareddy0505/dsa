class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxi=0
        count=0
        n=len(nums)
        for i in range(0, n):
            if nums[i] == 1:
                count += 1
                maxi=max(maxi,count)
            else:
                count=0
        return maxi
arr=[1,1,0,0,1,1,1,0]
sol=Solution()
print("resulting array is:",sol.findMaxConsecutiveOnes(arr))