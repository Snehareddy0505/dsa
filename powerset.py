def powerset(nums):
    n = len(nums)
    ans = []

    for mask in range(1 << n):      # 0 to 2^n - 1
        subset = []
        for i in range(n):
            if mask & (1 << i):     # check ith bit
                subset.append(nums[i])
        ans.append(subset)

    return ans
nums = [1, 2, 3]
print(powerset(nums))
