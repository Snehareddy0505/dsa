class Solution:
    def intersectionArray(self, A, B):
        i = 0
        j = 0
        m = len(A)
        n = len(B)
        ans = []

        while i < m and j < n:
            if A[i] < B[j]:
                i += 1
            elif B[j] < A[i]:
                j += 1
            else:
                ans.append(A[i])
                i += 1
                j += 1

        return ans

A = [1, 2, 2, 3, 3, 4, 5, 6]
B = [2, 3, 3, 5, 6, 6, 7]

sol = Solution()
print("resulting array is:", sol.intersectionArray(A, B))
            