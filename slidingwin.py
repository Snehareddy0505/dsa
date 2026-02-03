class Solution:
    def slidingwindow(self, arr, k):
        n = len(arr)
        result = []

        for i in range(n - k + 1):
            maxi = arr[i]
            for j in range(i, i + k):
                maxi = max(maxi, arr[j])
            result.append(maxi)
        return result
arr = list(map(int, input().split()))
k = int(input())

sol = Solution()
print(sol.slidingwindow(arr, k))

