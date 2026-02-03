class Solution:
    def numbersSum(self, N):
        #your code goes here
        if N == 0:
            return 0
        else:
            return N + self.numbersSum(N-1)
sol=Solution()
N=4
ans=sol.numbersSum(N)
print(ans)
    