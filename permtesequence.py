def permutesequence(n, k):
    fact = 1
    nums = []

    # calculate (n-1)! and store numbers 1 to n
    for i in range(1, n):
        fact *= i
        nums.append(i)
    nums.append(n)

    ans = ""
    k = k - 1   # convert to 0-based index

    while True:
        index = k // fact
        ans += str(nums[index])
        nums.pop(index)

        if len(nums) == 0:
            break

        k = k % fact
        fact = fact // len(nums)

    return ans
print(permutesequence(3, 3))

