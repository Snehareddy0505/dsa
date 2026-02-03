def subsetsWithDup(nums):
    nums.sort()          # important to handle duplicates
    res = []
    n = len(nums)

    def solve(ind, ds):
        if ind == n:
            res.append(ds.copy())
            return

        # 👉 TAKE current element
        ds.append(nums[ind])
        solve(ind + 1, ds)
        ds.pop()

        # 👉 NOT TAKE current element
        # skip all duplicates of nums[ind]
        next_ind = ind + 1
        while next_ind < n and nums[next_ind] == nums[ind]:
            next_ind += 1

        solve(next_ind, ds)

    solve(0, [])
    return res


nums = [1, 2, 2]
print(subsetsWithDup(nums))
