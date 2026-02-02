class Solution:
    def singleNumber(self, nums):
        #your code goes here
        XOR=0
        n=len(nums)
        for i in range(0, n):
            XOR=XOR^nums[i]
        return XOR
arr=[1,2,2,4,3,1,4]
sol=Solution()
print("resulting array is:",sol.singleNumber(arr))
