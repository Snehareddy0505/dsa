class Solution:
    def rotatematrix(self, matrix):
        n = len(matrix)

        # Create an empty matrix of same size
        ans = [[0] * n for _ in range(n)]

        # Fill ans matrix with rotated values
        for i in range(n):
            for j in range(n):
                ans[j][n - 1 - i] = matrix[i][j]

        return ans

# Input matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sol = Solution()
rotated = sol.rotatematrix(matrix)

print("Rotated matrix is:")
for row in rotated:
    print(row)
