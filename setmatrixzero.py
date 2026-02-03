class Solution:
    def setmatrixzero(self, nums):
        n = len(nums)
        m = len(nums[0])
        col0 = 1

        # Step 1: Mark the first row and first column
        for i in range(n):
            for j in range(m):
                if nums[i][j] == 0:
                    nums[i][0] = 0
                    if j != 0:
                        nums[0][j] = 0
                    else:
                        col0 = 0

        # Step 2: Set zeroes based on markers (excluding first row/col)
        for i in range(1, n):
            for j in range(1, m):
                if nums[i][0] == 0 or nums[0][j] == 0:
                    nums[i][j] = 0

        # Step 3: Handle the first row
        if nums[0][0] == 0:
            for j in range(m):
                nums[0][j] = 0

        # Step 4: Handle the first column
        if col0 == 0:
            for i in range(n):
                nums[i][0] = 0
nums = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 0, 16]
]

sol = Solution()
sol.setmatrixzero(nums)

for row in nums:
    print(row)   