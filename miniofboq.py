class Solution:
    def minDays(self, arr, r, b):
        def possible(arr, day, r, b):
            bouquets = 0
            flowers = 0
            for bloom in arr:
                if bloom <= day:
                    flowers += 1
                    if flowers == b:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= r

        if r * b > len(arr):
            return -1  # Not enough flowers to make r bouquets

        low = min(arr)
        high = max(arr)
        result = -1

        while low <= high:
            mid = (low + high) // 2
            if possible(arr, mid, r, b):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result

sol = Solution()
print(sol.minDays([1, 10, 3, 10, 2], 3, 1))  # Output: 3
print(sol.minDays([1, 10, 3, 10, 2], 3, 2))  # Output: -1
