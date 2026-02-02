class Solution:
    def subarray(self,nums):
        n=len(nums)
        cnt=0
        for i in range(0,n): 
            for j in range(i,n):
                total=0
                for k in range(i,j+1):
                    total+=nums[k]
                if total == 0:
                    cnt+=1
        return cnt
nums=[1,2,3,-3,1,1,1,4,2,-3]
sol=Solution() 
print("result array is:",sol.subarray(nums))