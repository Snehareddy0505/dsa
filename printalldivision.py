import math
class Solution:
    def divisors(self, n):
        result=[]
        for i in range(1,int(math.isqrt(n))+1):
            if n%i==0:
                result.append(i)
                if i != n//i:
                    result.append(n//i)
        return sorted(result)
n=36
sol=Solution()
print("result  is:",sol.divisors(n))

