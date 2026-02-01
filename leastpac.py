class Solution:
    def leastcapacity(self, arr, days):
        def days_needed(capacity):
            current = 0
            required_days = 1
            for weight in arr:
                if current + weight > capacity:
                    required_days += 1
                    current = 0
                current += weight
            return required_days

        low = max(arr)
        high = sum(arr)

        while low <= high:
            mid = (low + high) // 2
            nofdays = days_needed(mid)
            if nofdays <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low
sol = Solution()
print(sol.leastcapacity([1,2,3,1,1], 4))  
