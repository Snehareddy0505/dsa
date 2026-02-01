class Solution:
    def kthmissingnumber(self, arr, k):
        n = len(arr)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            # The number of missing elements before index mid
            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        # After the loop, 'low' is the index where the k-th missing number would go
        return low + k
sol = Solution()
print(sol.kthmissingnumber([2, 3, 4, 7, 11], 5))
