class Solution:
    def cntsubseqwithsumisk(self, ind, s, target, arr, n):
        # Base case
        if ind == n:
            if s == target:
                return 1
            return 0

        # Include current element
        left = self.cntsubseqwithsumisk(ind + 1, s + arr[ind], target, arr, n)

        # Exclude current element
        right = self.cntsubseqwithsumisk(ind + 1, s, target, arr, n)

        return left + right
arr = [1, 2, 1]
target = 2
n = len(arr)

sol = Solution()
print(sol.cntsubseqwithsumisk(0, 0, target, arr, n))
                                                                                                