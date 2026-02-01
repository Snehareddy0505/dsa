class Solution:
    def minsorted(self, arr, n):
        low = 0
        high = n - 1
        ans = float('inf')  # Correct INT_MAX to float('inf')
        
        while low <= high:
            mid = (low + high) // 2
            
            # If the subarray is already sorted
            if arr[low] <= arr[high]:
                ans = min(ans, arr[low])
                break  # No need to continue; the min is at low
            # Left part is sorted
            if arr[low] <= arr[mid]:
                ans = min(ans, arr[low])
                low = mid + 1
            # Right part is sorted
            else:
                ans = min(ans, arr[mid])
                high = mid - 1   
        return ans
arr = [4, 5, 6, 7, 0, 1, 2]
n = len(arr)
sol = Solution()
print(sol.minsorted(arr, n))  # Output: 0

