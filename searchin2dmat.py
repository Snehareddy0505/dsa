class Solution:
    def search2DMatrix(self, mat, target):
        n = len(mat)
        m = len(mat[0]) if n > 0 else 0

        low = 0
        high = n * m - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m

            if mat[row][col] == target:
                return True
            elif mat[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
sol = Solution()
mat = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
print(sol.search2DMatrix(mat, 9))  


