class Solution:
    def arrayrotated(self, arr):
        n = len(arr)
        low = 0
        high = n - 1
        ans = float('inf')
        index = -1

        while low <= high:
            mid = (low + high) // 2

            # If subarray is already sorted
            if arr[low] <= arr[high]:
                if arr[low] < ans:
                    ans = arr[low]
                    index = low
                break

            # If left part is sorted
            if arr[low] <= arr[mid]:
                if arr[low] < ans:
                    ans = arr[low]
                    index = low
                low = mid + 1
            else:
                # Right part is sorted
                if arr[mid] < ans:
                    ans = arr[mid]
                    index = mid
                high = mid - 1

        return ans,index
arr = [4, 5, 6, 7, 0, 1, 2]
sol = Solution()
print(sol.arrayrotated(arr))  # Output: (0, 4)

