def singlenumber3(nums):
    freq = {}

    # count frequency
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    ans = []
    # collect elements that appear once
    for key, value in freq.items():
        if value == 1:
            ans.append(key)

    return ans
nums = [1, 2, 1, 3, 2, 5]
print(singlenumber3(nums))
