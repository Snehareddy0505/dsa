class Solution:
    def longestConsecutive(self, nums):
        n=len(nums)
        if n==0:
            return 0
        st = set()
        for num in nums:
            st.add(num)
        longest=1
        for it in st:
            if(it-1)not in st:
                x=it
                cnt=1
                while(x+1) in st:
                    x+=1
                    cnt+=1
                longest=max(longest,cnt)          
        return longest
nums=[100,4,200,1,3,2]
sol=Solution()
print("longest is:",sol.longestConsecutive(nums))  