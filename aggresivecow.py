class Solution:
    def can_we_place(self, arr, dist, cows):
        count = 1  # place first cow at the first stall
        last_pos = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] - last_pos >= dist:
                count += 1
                last_pos = arr[i]
                if count == cows:
                    return True
        return False

    def aggressive_cow(self, arr, cows):
        arr.sort()
        low = 1  # Minimum possible distance
        high = arr[-1] - arr[0]  # Maximum possible distance
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if self.can_we_place(arr, mid, cows):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
sol = Solution()
arr = [1, 2, 8, 4, 9]
cows = 3
print(sol.aggressive_cow(arr, cows))  # Output: 3
  
            