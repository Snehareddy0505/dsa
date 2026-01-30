class Solution:
    def armstrongnumber(self, n):
        dupnum=n
        sum=0
        while n>0:
            lastdigit=n%10
            n=n//10
            sum=sum+(lastdigit*lastdigit*lastdigit)
        if sum==dupnum:
            return True
        else:
            return False
n=35
sol=Solution()
print("result  is:",sol.armstrongnumber(n))