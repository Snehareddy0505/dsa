class Solution:
    def majorityElement(self, nums):
        count_map={}
        n=len(nums)
        for num in nums:
            count_map[num]=count_map.get(num,0)+1

        for key,value in count_map.items():
            if value>n//2:
                return key
        return -1
arr=[1,1,1,2,1,2]
sol=Solution()
print("result  is:",sol.majorityElement(arr))    