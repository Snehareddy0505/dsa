from collections import deque

class Solution:
    def slidingwindow(self, arr, k):
        n = len(arr)
        result = []          # to store answers
        dq = deque()         # will store indices

        for i in range(n):

            # 1. Remove elements out of current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Remove smaller elements (they are useless)
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Window complete → store maximum
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
arr = [1,3,-1,-3,5,3,6,7]
k = 3
sol = Solution()
print(sol.slidingwindow(arr, k))

