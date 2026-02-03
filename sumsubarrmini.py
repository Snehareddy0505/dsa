class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        total = 0

        for i in range(0, n):
            mini = arr[i]
            for j in range(i, n):
                mini = min(mini, arr[j])
                total = total + mini

        return total

arr=list(map(int,input().split()))
sol=Solution()
print(sol.sumSubarrayMins(arr))