class Solution:
    def rearrangeArray(self, nums):
        pos = []
        neg = []

        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        result = []
        i = j = 0

        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i += 1
            j += 1

        # append remaining elements
        while i < len(pos):
            result.append(pos[i])
            i += 1

        while j < len(neg):
            result.append(neg[j])
            j += 1

        return result

nums=[2,-1,5,-3,-4]
sol=Solution()
print("result is:",sol.rearrangeArray(nums))