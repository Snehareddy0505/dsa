class Solution:
    def subseq(self, ind, ds, s, target, arr, n):
        # Base case
        if ind == n:
            if s == target:
                print(ds)
            return
        
        # Include current element
        ds.append(arr[ind])
        self.subseq(ind + 1, ds, s + arr[ind], target, arr, n)
        
        # Backtrack
        ds.pop()
        
        # Exclude current element
        self.subseq(ind + 1, ds, s, target, arr, n)
arr = [1, 2, 1]
target = 2
n = len(arr)

sol = Solution()
sol.subseq(0, [], 0, target, arr, n)
