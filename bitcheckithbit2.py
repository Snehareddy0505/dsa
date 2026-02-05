class Solution:
    def checkthBit(self,n,k):
        if(n&(1<<k)==0):
            return False
        return True
sol=Solution()
print("checkthBit:",sol.checkthBit(13,2))