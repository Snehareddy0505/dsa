class Solution:
    def setkthBit(self,n,k):
        return n|(1<<k)
sol=Solution()
print("setkthBit:",sol.setkthBit(13,2))