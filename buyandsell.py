class Solution:
    def stockBuySell(self, arr, n):
       mini=arr[0]
       profit=0
       for i in range(0,n):
          cost=arr[i]-mini
          profit=max(profit,cost)
          mini=min(mini,arr[i])
       return profit
arr=[10,7,5,8,11,9]
n=len(arr)
sol=Solution()
print("result is:",sol.stockBuySell(arr,n))