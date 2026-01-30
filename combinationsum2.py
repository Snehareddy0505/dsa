def combinationSum2(candidates, target):
    candidates.sort()
    ans = []

    def solve(ind, target, ds):
        if target == 0:
            ans.append(ds.copy())
            return
        
        for i in range(ind, len(candidates)):
            # Skip duplicates
            if i > ind and candidates[i] == candidates[i-1]:
                continue
            
            # Prune recursion
            if candidates[i] > target:
                break
            
            ds.append(candidates[i])
            solve(i + 1, target - candidates[i], ds)
            ds.pop()

    solve(0, target, []) 
    return ans
candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates, target))

