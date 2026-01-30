def cntnumofnicsubarr(nums, goal):
    if goal < 0:
        return 0

    l = 0
    curr_sum = 0
    cnt = 0

    for r in range(len(nums)):
        curr_sum += nums[r] % 10

        while curr_sum > goal:
            curr_sum -= nums[l] % 10
            l += 1

        cnt += (r - l + 1)

    return cnt
nums = [12, 15, 23, 40, 11]
k = 2

print(cntnumofnicsubarr(nums, k))
