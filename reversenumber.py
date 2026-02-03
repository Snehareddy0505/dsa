class Solution:
    def reverseNumber(self, n):
        reversenum=0
        while n>0:
            lastdigit=n%10
            n=n//10
            reversenum=reversenum*10+lastdigit
        return reversenum
n=25
sol=Solution()
print("result  is:",sol.reverseNumber(n))