def subsets(nums):
    res = []
    n = len(nums)

    def solve(ind, ds):
        if ind == n:
            res.append(ds.copy())
            return

        # not take
        solve(ind + 1, ds)

        # take
        ds.append(nums[ind])
        solve(ind + 1, ds)
        ds.pop()

    solve(0, [])
    return res


nums = [1, 2, 3]
print(subsets(nums))


