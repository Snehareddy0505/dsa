def singlenumber3(nums):
    xorr = 0

    # Step 1: XOR of all elements
    for num in nums:
        xorr ^= num

    # Step 2: Find rightmost set bit
    rightmost = xorr & -xorr

    b1 = 0
    b2 = 0

    # Step 3: Divide numbers into two groups
    for num in nums:
        if num & rightmost:
            b1 ^= num
        else:
            b2 ^= num

    return b1, b2
nums = [1, 2, 1, 3, 2, 5]
print(singlenumber3(nums))