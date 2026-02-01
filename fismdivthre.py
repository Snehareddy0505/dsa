import math

def smallestDivisor(arr, threshold):
    def compute_sum(divisor):
        return sum(math.ceil(num / divisor) for num in arr)

    low = 1
    high = max(arr)
    ans = high  # initialize with the max value, will store the minimum valid divisor

    while low <= high:
        mid = (low + high) // 2
        if compute_sum(mid) <= threshold:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
print(smallestDivisor([1, 2, 5, 9], 6))  # Output: 5
