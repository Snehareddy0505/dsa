class Solution:
    def peakelement(self, mat, n, m):
        low = 0
        high = m - 1

        while low <= high:
            mid = (low + high) // 2

            # Find the row index of the maximum element in mid column
            max_row = 0
            for i in range(1, n):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            # Get left and right neighbors (if any)
            left = mat[max_row][mid - 1] if mid - 1 >= 0 else float('-inf')
            right = mat[max_row][mid + 1] if mid + 1 < m else float('-inf')

            # Check if current element is a peak
            if mat[max_row][mid] >= left and mat[max_row][mid] >= right:
                return (max_row, mid)
            elif left > mat[max_row][mid]:
                high = mid - 1
            else:
                low = mid + 1

        return (-1, -1)
sol = Solution()
mat = [
    [10, 8, 10, 10],
    [14, 13, 12, 11],
    [15, 9, 11, 21],
    [16, 17, 19, 20]
]
n = 4
m = 4
print(sol.peakelement(mat, n, m))  
