class Solution:
    def printTriangle(self, N):
        # Code here
        N=5
        for row in range(1,N+1):
           for col in range(1,N-row+2):
            print(col,end=" ")
           print()
sol = Solution()
sol.printTriangle(5)
