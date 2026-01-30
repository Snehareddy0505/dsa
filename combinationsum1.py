def combinationSum(candidates, target):
    n = len(candidates)

    def solve(ind, target, ds):
        if ind == n:
            if target == 0:
                print(ds)   # PRINT RESULT
            return

        # pick the element
        if candidates[ind] <= target:
            ds.append(candidates[ind])
            solve(ind, target - candidates[ind], ds)
            ds.pop()   # backtrack

        # not pick the element
        solve(ind + 1, target, ds)

    solve(0, target, [])


# Driver code
candidates = [2, 3, 6, 7]
target = 7
combinationSum(candidates, target)
