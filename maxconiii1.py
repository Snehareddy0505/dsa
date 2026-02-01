def maxconsecutive(nums, k):
    n = len(nums)
    maxlen = 0

    for i in range(n):
        zeros = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1

            if zeros <= k:
                curr_len = j - i + 1
                maxlen = max(maxlen, curr_len)
            else:
                break

    print(maxlen)


nums = [1, 1, 1, 0, 0, 1, 1, 0, 0]
k = 2
maxconsecutive(nums, k)

