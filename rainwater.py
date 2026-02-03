height=list(map(int,input().split()))
n=len(height)
left=[0]*n
left[0]=height[0]
for i in range(1,n):
    left[i]=max(left[i-1],height[i])
right=[0]*n
right[n-1]=height[n-1]
for i in range(n-2,-1,-1):
    right[i]=max(right[i+1],height[i])
water_tapped=0
for i in range(0,n):
    water_tapped+=min(left[i],right[i])-height[i]
print(water_tapped)