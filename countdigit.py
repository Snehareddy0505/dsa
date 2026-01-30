class Solution:
    def countDigit(self, n):
        c=0
        while n>0:
            n=n//10
            c+=1
        return c
n=123
sol=Solution()
print("result  is:",sol.countDigit(n))