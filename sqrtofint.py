class Solution:
    def sqrtnum(self,n):
        low=1   
        high=n
        ans=1
        while low<=high:
            mid=(low+high)//2
            if mid*mid<=n:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
sol = Solution()
print(sol.sqrtnum(16))  # Output: 4
print(sol.sqrtnum(10))  # Output: 3
print(sol.sqrtnum(25))  # Output: 5
print(sol.sqrtnum(27))  # Output: 5
