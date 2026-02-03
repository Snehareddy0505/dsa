class Solution:
    def subseqwhosesumissum(self, ind, ds, s, target, arr, n):
        # Base case
        if ind == n:
            if s == target:
                print(ds)
                return True
            return False

        # Include current element
        ds.append(arr[ind])
        if self.subseqwhosesumissum(ind + 1, ds, s + arr[ind], target, arr, n):
            return True

        # Backtrack
        ds.pop()

        # Exclude current element
        if self.subseqwhosesumissum(ind + 1, ds, s, target, arr, n):
            return True

        return False
arr = [1, 2, 1]
target = 2
n = len(arr)

sol = Solution()
sol.subseqwhosesumissum(0, [], 0, target, arr, n)
