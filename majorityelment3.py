class Solution:
    def majorityElement(self, nums):
        cnt=0
        el=None
        for num in nums:
            if cnt==0:
                el=num
                cnt=1
            elif el==num:
                cnt+=1
            else:
                cnt-=1
        if nums.count(el)>len(nums)//2:
            return el
        else:
         return -1
arr=[1,1,1,2,1,2]
sol=Solution()
print("result  is:",sol.majorityElement(arr))  