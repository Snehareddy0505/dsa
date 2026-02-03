class Solution:
    def  sortZeroOneTwo(self, a):
           n=len(a)
           low=0
           mid=0
           high=n-1
           while mid<=high:
            if a[mid]==0:
                a[mid],a[low]=a[low],a[mid]
                low+=1
                mid+=1
            elif a[mid]==1:
                mid+=1
            else:
                a[mid]==2
                a[mid],a[high]=a[high],a[mid]
                high-=1
           return a
arr=[1,0,2,1,0]
sol=Solution()
print("result is:",sol.sortZeroOneTwo(arr))
                   
