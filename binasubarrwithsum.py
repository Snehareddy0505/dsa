def binsubarrwithsum(nums, goal):
    if goal < 0:
        return 0

    l = 0
    curr_sum = 0
    cnt = 0

    for r in range(len(nums)):
        curr_sum += nums[r]

        while curr_sum > goal:
            curr_sum -= nums[l]
            l += 1

        cnt += (r - l + 1)

    return cnt
nums = [1,0,1,0,1]
goal = 2

print(binsubarrwithsum(nums, 2))   # atMost(2)
print(binsubarrwithsum(nums, 1))   # atMost(1)
