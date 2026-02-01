class Solution:
    def longestSubarray(self, nums, k):
        left=0
        right=0
        total=0
        maxlen=0
        n=len(nums)
        while right < n:
            total += nums[right]
            while total > k and  left <= right:
                    total -= nums[left]
                    left += 1
            if total == k:
                maxlen=max(maxlen,right-left+1)
            right += 1
        return maxlen
arr=[10,5,2,7,1,9]
sol=Solution()
print("resulting array is:",sol.longestSubarray(arr, 15))

            
        