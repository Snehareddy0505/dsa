class Solution:
    def selectionsort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            mini = i
            for j in range(i + 1, n):
                if arr[j] < arr[mini]:
                    mini = j
            arr[i], arr[mini] = arr[mini], arr[i]
        return arr

arr = [12, 54, 32, 65]
sol = Solution()
print("result is:", sol.selectionsort(arr))
                