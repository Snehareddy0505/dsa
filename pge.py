nums=list(map(int,input().split()))
stack=[]
n=len(nums)
ans=[0]*n
for i in range(0,n):
    while(len(stack)!=0 and stack[-1]<=nums[i]):
        stack.pop()
    if(len(stack)==0):
        ans[i]=-1
    else:
        ans[i]=stack[-1]
    stack.append(nums[i])
print(ans)
        