class Solution:
    def reverseNumber(self, n):
        dupnum=n
        reversenum=0
        while n>0:
            lastdigit=n%10
            reversenum=reversenum*10+lastdigit
            n=n//10
        if reversenum==dupnum:
            return True
        else:
            return False
n=123321
sol=Solution()
print("result  is:",sol.reverseNumber(n))