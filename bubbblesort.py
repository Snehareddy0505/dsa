class Solution:
    def Bubblesort(self, arr):
        n = len(arr)
        for i in range(n - 1, 0, -1):
            didswap = False
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    didswap = True
            if not didswap:
                break
        return arr
arr = [12, 54, 32, 65]
sol = Solution()
print("result is:", sol.Bubblesort(arr))
