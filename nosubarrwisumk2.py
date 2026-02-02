class Solution:
    def subarray(self,nums,k):
        n=len(nums)
        mpp={0:1}
        presum=0
        cnt=0
        for num in nums:
            presum+=num
            remove=presum-k
            if remove in mpp:
              cnt+=mpp[remove]
            mpp[presum]=mpp.get(presum,0)+1
        return cnt
nums=[1,2,3,-3,1,1,1,4,2,-3]
sol=Solution()
print("result array is:",sol.subarray(nums,0))