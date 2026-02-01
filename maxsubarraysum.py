class Solution:
    def maxSubArray(self, nums):
        maxi=float('-inf')
        sum=0
        start=0
        ans_start=0
        ans_end=0
        for i in range(len(nums)):
            if sum==0:
                start = i
                sum+=nums[i]
            if sum>maxi:
                maxi=sum
                ans_start=start
                ans_end=i
            if sum<0:
                sum=0
        print("subarray with max sum is:", nums[ans_start:ans_end+1])
        return maxi
arr=[2,3,5,-2,7,-4]
sol=Solution()
print("result is:",sol.maxSubArray(arr)) 
