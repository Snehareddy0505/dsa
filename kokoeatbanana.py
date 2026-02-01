import math
class Solution:
    def fun(self, arr, speed):
        total_hours = 0
        for i in range(len(arr)):
            total_hours += math.ceil(arr[i] / speed)
        return total_hours

    def binarysearch(self, arr, h):
        low = 1
        high = max(arr)
        ans = float('inf')

        while low <= high:
            mid = (low + high) // 2
            total_hours = self.fun(arr, mid)

            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
arr=[3,6,7,11]
sol=Solution()
print(sol.binarysearch(arr,8))
