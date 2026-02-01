def maxconsecutive(nums, k):
    left = 0
    right = 0
    zeros = 0
    maxlen = 0

    while right < len(nums):
        if nums[right] == 0:
            zeros += 1

        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        maxlen = max(maxlen, right - left + 1)
        right += 1

    print(maxlen)
nums = [1, 1, 1, 0, 0, 1, 1, 0, 0]
k = 2
maxconsecutive(nums, k)
