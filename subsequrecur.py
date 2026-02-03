class Solution:
    def subsequence(self, ind, ds, arr, n):
        if ind == n:
            print(ds)
            return

        # take the element
        ds.append(arr[ind])
        self.subsequence(ind + 1, ds, arr, n)

        # not take the element
        ds.pop()
        self.subsequence(ind + 1, ds, arr, n)


# Driver code
arr = [3, 1, 2]
n = len(arr)
ds = []

sol = Solution()
sol.subsequence(0, ds, arr, n)
