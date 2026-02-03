class Solution:
    def sumsubarrrange(self, arr):
        n = len(arr)
        total = 0

        for i in range(0, n):
            largest = arr[i]
            smallest = arr[i]

            for j in range(i + 1, n): 
                largest = max(largest, arr[j])
                smallest = min(smallest, arr[j])
                total = total + (largest - smallest)

        return total
arr = list(map(int, input().split()))
sol = Solution()
print(sol.sumsubarrrange(arr))
