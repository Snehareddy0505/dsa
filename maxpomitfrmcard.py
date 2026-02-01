def maxpointfromcard(nums, k):
    lsum = 0
    rsum = 0
    maxsum = 0
    n = len(nums)

    # take first k elements from left
    for i in range(0, k):
        lsum = lsum + nums[i]
    maxsum = lsum

    rindex = n - 1

    # remove one from left and add one from right
    for i in range(k - 1, -1, -1):
        lsum = lsum - nums[i]
        rsum = rsum + nums[rindex]
        rindex = rindex - 1

        maxsum = max(maxsum, lsum + rsum)

    return maxsum
nums = [1,2,3,4,5,6,1]
k = 3
print(maxpointfromcard(nums, k))
