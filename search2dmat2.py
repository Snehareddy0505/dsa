class Solution:
    def search2DMatrix(self,mat,target):
        n=len(mat)
        m=len(mat[0]) 
        row=0
        col=m-1
        while row<n and col>=0:
            if mat[row][col]==target:
                return True
            elif mat[row][col]<target:
                row+=1
            else:
                col-=1
        return False
sol=Solution()
mat = [
    [1,  4,  7, 11],
    [2,  5,  8, 12],
    [3,  6,  9, 16],
    [10,13, 14,17]
]
print(sol.search2DMatrix(mat,9))
