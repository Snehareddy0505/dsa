def moveZeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums

arr = [1,0,2,3,2,0,0,4,5,1]
print(moveZeroes(arr))
