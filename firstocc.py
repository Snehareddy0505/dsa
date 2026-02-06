class Solution:
    def searchRange(self, nums, target):
        def lowerbound(nums,target):
            n=len(nums)
            low=0
            high=n-1
            ans=n
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        def upperbound(nums,target):
            n=len(nums)
            low=0
            high=n-1
            ans=n
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        lb = lowerbound(nums,target)
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        ub = upperbound(nums,target)
        return [lb, ub - 1]