class Solution:
  def fact(self,n):
    if n==0:
        return 1
    else:
        return n*self.fact(n-1)
sol=Solution()
n=5
print("result is:",sol.fact(n))