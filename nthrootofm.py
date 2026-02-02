class Solution:
    def power(self, mid, n):
        # Returns mid^n (without using **)
        ans = 1
        for _ in range(n):
            ans *= mid
        return ans

    def nthRootElement(self, n, m):
        low = 1
        high = m

        while low <= high:
            mid = (low + high) // 2
            mid_power = self.power(mid, n)

            if mid_power == m:
                return mid  # Found exact root
            elif mid_power < m:
                low = mid + 1
            else:
                high = mid - 1

        return high  # Return floor of nth root if exact root not found
sol = Solution()
print(sol.nthRootElement(3, 27))  # Output: 3 (since 3^3 = 27)
print(sol.nthRootElement(2, 16))  # Output: 4
print(sol.nthRootElement(3, 30))  # Output: 3 (since 3^3 = 27 < 30 < 4^3 = 64)

