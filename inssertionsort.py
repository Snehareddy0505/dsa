class Solution:
    def insertionsort(self,arr):
        n=len(arr)
        for i in range(0,n-1):
            j=i
            while j>0 and arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
        return arr
arr = [12, 54, 32, 65]
sol = Solution()
print("result is:", sol.insertionsort (arr))