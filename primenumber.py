class Solution:
    def isPrime(self, n):
        cnt=0
        for i in range(1,n+1):
            if n%i==0:
                cnt+=1
        if cnt==2: 
            return True
        else:
            return False
n=3
sol=Solution()
print("result  is:",sol.isPrime(n))
